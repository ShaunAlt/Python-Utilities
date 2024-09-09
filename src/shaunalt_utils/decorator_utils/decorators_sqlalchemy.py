# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Decorators - SQLAlchemy
-
Contains the decorators that can be used for SQLAlchemy methods.

Contents
-
- `convert_id_to_model` : `(sqlalchemy.Column) -> (F) -> F`
    - Decorator for converting a given single column id into a 
    
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
None
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

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
    TYPE_CHECKING, # whether or not static type checking is enabled
    TypeVar, # type variable - used for custom defined types
)

# static type checking imports
if TYPE_CHECKING:
    # used for type hinting sqlalchemy types
    from sqlalchemy import Column # type: ignore # ORM table column
else: Column = Any


# =============================================================================
# Type Definitions
# =============================================================================
F = TypeVar('F', bound = Callable[..., Any])


# =============================================================================
# ID to BaseModel
# =============================================================================
def convert_id_to_basemodel(col: Column) -> Callable[[F], F]:
    '''
    ID to BaseModel
    -
    Decorator for converting a given single column id into a `BaseModel`.

    Parameters
    -
    - col : `sqlalchemy.Column`
        - `BaseModel.col_name`. This is the column object that will be used
            to filter the `idx` parameter to get the `BaseModel` object.

    Returns
    -
    - `(F) -> F`
        - Decorated function.
    '''

    # internal decorator
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # get idx from kwargs
            idx: Optional[int] = None
            try:
                if 'idx' in kwargs:
                    if kwargs['idx'] is not None:
                        idx = int(kwargs['idx'])
            except
            idx = kwargs.pop('idx') # type: ignore # remove idx from kwargs
            model = col.type.mapper.class_(id=idx) # type: ignore # get BaseModel instance
            kwargs['model'] = model # add model to kwargs
            return func(*args, **kwargs)
        return cast(F, wrapper)
    return decorator


# =============================================================================
# End of File
# =============================================================================
