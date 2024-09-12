# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Errors - Default Handler
-
Contains the method that can be used to simplify the handling of errors.

Contents
-
- error_handler(e, desc, log, **kwargs) : `Exception`
    - Creates a new `Exception` containing keyword data pertaining to the
        exception that was raised.
    
Dependencies
-
- `logging`
    - Used for creating / getting loggers.
    - Builtin.
- `typing`
    - Used for type hinting.
    - Builtin.

Internal Dependencies
-
- `generic_utils`
    - Used for base object definition.
    - `generic_utils`.
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

# used for base object definition
from ..generic_utils import OBJ

# used for creating / getting loggers
import logging

# used for type hinting
from typing import (
    Any, # any type
    List, # list type
    Type, # type of object type
)


# =============================================================================
# Default Error Handler
# =============================================================================
def error_handler(
        e: Type[Exception],
        desc: str,
        log: logging.Logger,
        **kwargs: Any
) -> Exception:
    '''
    Default Error Handler
    -
    Creates a new `Exception` containing keyword data pertaining to the
    exception that was raised.

    Parameters
    -
    - e : `Type[Exception]`
        - Type of `Exception` to be raised.
    - desc : `str`
        - Short description of the error that occurred.
    - log : `logging.Logger`
        - Logger to be used to log the error that occurred.
    - **kwargs : `Any`
        - Collection of keyword arguments to parse as additional messages to
            the exception.

    Returns
    -
    - `Exception`
        - New exception containing all of the keyword data.
    '''

    # create error strings
    error_strings: List[str] = [desc]
    for key, val in kwargs.items():
        if isinstance(val, OBJ): error_strings.append(f'{key} = {val.debug()}')
        else: error_strings.append(f'{key} = {val!r}')

    # log error message
    log.error(
        f'Error Occurred: {e.__name__}\n\t' \
        + '\n\t'.join([
            err_str.replace('\n', '\n\t')
            for err_str in error_strings
        ]),
        exc_info = True
    )

    return e(*error_strings)


# =============================================================================
# End of File
# =============================================================================
