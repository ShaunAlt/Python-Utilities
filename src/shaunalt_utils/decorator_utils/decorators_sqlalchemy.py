# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Decorators - SQLAlchemy
-
Contains the decorators that can be used for SQLAlchemy methods.

Contents
-
- `sqlalchemy_id_to_model` : `(sqlalchemy.Column, str, str, bool) -> (F) -> F`
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

# used for custom errors
from .errors import (
    InvalidIDError, # invalid id
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
def sqlalchemy_id_to_basemodel(
        col: Column,
        param_name_idx: str = 'idx',
        param_name_item: str = 'item',
        nullable: bool = True
) -> Callable[[F], F]:
    '''
    ID to BaseModel
    -
    Decorator for converting a given single column id into a `BaseModel`.

    Parameters
    -
    - col : `sqlalchemy.Column`
        - `BaseModel.col_name`. This is the column object that will be used
            to filter the `idx` parameter to get the `BaseModel` object.
    - param_name_idx : `str`
        - Defaults to `"idx"`, meaning that the keyword parameter that will be
            used to get the data from will be "idx".
    - param_name_item : `str`
        - Defaults to `"item"`, meaning that the `BaseModel` object retrieved
            from the idx will be stored under this keyword argument name.
    - nullable : `bool`
        - Defaults to `True`, meaning that if the `param_name_idx` value is not
            present, or the `param_name_idx` value results in a non-existent
            `BaseModel` object, the function will still run without error.

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
                if param_name_idx in kwargs:
                    if kwargs[param_name_idx] is not None:
                        idx = int(kwargs[param_name_idx])
            except:
                raise InvalidIDError(
                    f'Invalid {param_name_idx} Parameter Value'
                )

            # validate idx value
            if (idx is None) and (not nullable):
                raise InvalidIDError(f'{param_name_idx} Parameter is Required')

            # get model from idx
            obj: None = None
            raise NotImplementedError('sqlalchemy_id_to_basemodel() not fully defined')
            if (obj is None) and (not nullable):
                raise InvalidIDError(
                    f'IDX Parameter Value {param_name_idx} Resulted in ' \
                    + 'NoneType.'
                )
            kwargs[param_name_item] = obj

            # run function
            return func(*args, **kwargs)
        return cast(F, wrapper)
    return decorator


# =============================================================================
# End of File
# =============================================================================
