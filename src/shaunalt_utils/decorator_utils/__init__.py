# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Decorators
-
Contains a collection of methods that can be used as decorators for functions.

Contents
-
TODO: Fix this
- validate_idx
    - Outer/Inner decorator
    - @decorator1(extra_args,  ...) <- additional arguments to the decorator
    - def inner_func(...): ...
- flask error handler route decorator.
- sqlalchemy - convert id to `BaseModel` instance. Only works on tables with a
    single PK column. Takes the `BaseModel.col_pk` column as an argument, and
    uses it to get the `idx` parameter from the function parameters, and parse
    the `BaseModel|None` instance returned.

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
- `generic_utils`
    - Used for base + timing objects.
    - `generic_utils`.
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

# flask decorators
from .decorators_flask import (
    flask_error_handler, # flask route / method error handler
)

# generic decorators
from .decorators_generic import (
    method_timer, # method timer decorator
)

# sqlalchemy decorators
from .decorators_sqlalchemy import (
    sqlalchemy_id_to_basemodel, # convert to basemodel
)


# =============================================================================
# End of File
# =============================================================================
