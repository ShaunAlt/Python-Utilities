# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Decorators - SQLAlchemy
-
Contains the decorators that can be used for SQLAlchemy methods.

Contents
-
- `convert_id_to_model` : `(str | int | None, sqlalchemy.Column) -> BaseModel | None`
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
    TypeVar, # type variable - used for custom defined types
)


# =============================================================================
# Type Definitions
# =============================================================================
F = TypeVar('F', bound = Callable[..., Any])


# =============================================================================
# ID to BaseModel
# =============================================================================


# =============================================================================
# End of File
# =============================================================================
