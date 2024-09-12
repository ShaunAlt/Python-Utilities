# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Decorators - Flask
-
Contains the decorators that can be used for flask functions and routes.

Contents
-
- flask_error_handler : `(...) -> (F) -> F`
    - Decorator for handling exceptions raised in the decorated method, and
        then returning a `flask.abort` code.
    
Dependencies
-
- `flask`
    - Used for flask framework functionality.
    - `flask==3.0.3`
- `flask-login`
    - Used for getting the current user logged into the session.
    - `flask-login==0.6.3`
- `logging`
    - Used for creating / getting loggers.
    - Builtin.
- `typing`
    - Used for type hinting.
    - Builtin.
- `werkzeug`
    - Used for identifying werkzeug HTTP exceptions compared to regular errors.
    - `werkzeug==3.0.4`

Internal Dependencies
-
- `email_utils`
    - Used for sending emails.
    - `email_utils`.
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

# used for sending emails
from ..email_utils import Email

# used for wrapping functions in decorators
from functools import wraps

# used for creating / getting loggers
import logging

# used for type hinting
from typing import (
    Any, # any type
    Callable, # function type
    cast, # static type cast - not implemented at runtime
    List, # list type
    Optional, # optional data types
    TypeVar, # type variable - used for custom defined types
)


# =============================================================================
# Type Definitions
# =============================================================================
F = TypeVar('F', bound = Callable[..., Any])


# =============================================================================
# Flask Error Handler
# =============================================================================
def flask_error_handler(
        log: logging.Logger,
        abort_code: int = 500,
        display_cu: bool = True,
        display_req: bool = True,
        email_creator: Optional[Callable[[Exception], Email]] = None,
        flash_restart: bool = True,
        smtp_server: str = 'SMTP',
        smtp_port: int = 465,
        smtp_sender: str = 'noreply@hostname',
        smtp_bounce: Optional[str] = 'bounce@hostname'
) -> Callable[[F], F]:
    '''
    Flask Error Handler
    -
    Decorator for handling exceptions raised in the decorated method, and then
    returning a `flask.abort` code.

    Parameters
    -
    - log : `logging.Logger`
        - Error logger to use to log any errors that are raised by the
            decorated method.
    - abort_code : `int`
        - Defaults to `500`, which is typically used for "Internal Server
            Error" errors. This value is the abort code that is implemented by
            `flask.abort` if an unknown error is encountered.
    - display_cu : `bool`
        - Defaults to `True`, meaning that the `flask_login.current_user`
            object will be logged.
    - display_req : `bool`
        - Defaults to `True`, meaning that the `flask.request` object will be
            logged.
    - email_creator : `Callable[[Exception], Email] | None`
        - Defaults to `None`, meaning that no email will be sent when an error
            occurs. If not `None`, then this should be a custom function which
            will take the `Exception` that was raised, and return an email that
            can be sent to the required people.
    - flash_restart : `bool`
        - Defaults to `True`, meaning that all `flask.flash` messages that had
            been set will be cleared before the error is raised.

    Returns
    -
    - `(F) -> F`
        - Decorated function.
    '''

    # import flask dependencies
    from flask import (
        abort, # used to abort with a http error
        request, # used to get the http request data
        session, # used to get the flask session data
    )
    from flask_login import current_user # type: ignore # used for current user 
    from werkzeug.exceptions import HTTPException # http exception

    # internal decorator
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> F:
            # attempt to run function
            try: return func(*args, **kwargs)
            except Exception as e:
                # if the exception was already a http error (e.g. 404, 401)
                # then keep return that abort code instead of overriding
                if isinstance(e, HTTPException):
                    if e.code is None: abort(500)
                    abort(e.code)

                # create error messages
                error_strings: List[str] = [
                    f'Error Occurred: {e.__class__.__name__}',
                    f'Function: {func.__name__}',
                ]
                if display_cu:
                    error_strings.append(
                        'Current User = ' \
                        + repr(current_user).replace('\n', '\n\t')
                    )
                if display_req:
                    error_strings.append(
                        'Flask Request = ' \
                        + repr(request).replace('\n', '\n\t')
                    )

                # log the error
                log.error('\n\t'.join(error_strings))

                # clear + refresh flash messages if required
                if flash_restart:
                    if '_flashes' in session: session.pop('_flashes')

                # email error - if required
                if email_creator is not None:
                    email_creator(e).send(
                        smtp_server = smtp_server,
                        smtp_port = smtp_port,
                        smtp_sender = smtp_sender,
                        bounce_address = smtp_bounce
                    )

                # abort with failure code
                abort(abort_code)

        return cast(F, wrapper)
    return decorator


# =============================================================================
# End of File
# =============================================================================
