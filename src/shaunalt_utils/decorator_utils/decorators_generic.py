# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Decorators - Generic
-
Contains the decorators that can be used for generic methods.

Contents
-
None
    
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
    - Used for base + timing objects.
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

# used for base + timing objects
from ..generic_utils import (
    OBJ, # base object
    TIMER, # timing object
)

# used for wrapping functions in decorators
from functools import wraps

# used for creating / getting loggers
import logging

# used for type hinting
from typing import (
    Any, # any type
    Callable, # function type
    cast, # static type cast - not implemented at runtime
    Optional, # optional data types
    TypeVar, # type variable - used for custom defined types
)


# =============================================================================
# Type Definitions
# =============================================================================
F = TypeVar('F', bound = Callable[..., Any])


# =============================================================================
# Method Timer
# =============================================================================
def method_timer(
        log: logging.Logger,
        lvl: int = -1
) -> Callable[[F], F]:
    '''
    Method Timer
    -
    Decorator for timing the decorated method.

    Parameters
    -
    - log : `logging.Logger`
        - Logger to pass to the `TIMER` being created to time the decorated
            method.
    - lvl : `int`
        - `TIMER` verbosity indentation level.
    
    Returns
    -
    - `(F) -> F`
        - Decorated function.
    '''

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> F:
            with TIMER(func.__name__, log, lvl): return func(*args, **kwargs)
        return cast(F, wrapper)
    return decorator


# =============================================================================
# End of File
# =============================================================================
