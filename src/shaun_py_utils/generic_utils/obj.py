# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Generic - Base Object
-
Contains the definition for the base object that all other objects can inherit
from.

Contents
-
- to_str(obj, lvl) : `str`
    - Converts a single object to a single or multiple line string. Used by the
        `OBJ.__repr__`, `OBJ.__str__`, and `OBJ.debug` methods.
- `OBJ`
    - Represents a base object with generic functionality that all other
        objects can inherit from.
    
Dependencies
-
- `__future__`
    - Used for string type hints.
    - Builtin.
- `types`
    - Used for type hinting.
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

# used for string type hints
from __future__ import annotations

# used for type-hinting traceback types
from types import TracebackType

# used for type-hinting
from typing import (
    Any, # any type
    Dict, # dictionary type
    Optional, # optional type
    Type, # type-hinted type
)


# =============================================================================
# Object to String Converter
# =============================================================================
def to_str(obj: Any, lvl: int) -> str:
    '''
    Object to String Converter
    -
    Converts a single object to a single or multiple line string. Used by the
    `__repr__` and `__str__` methods in `OBJ`.

    Parameters
    -
    - obj : `Any`
        - Object being converted to a string.
    - lvl : `int`
        - Verbosity level with which to output the data.
        - If `0`, then output will be a short single line string.
        - If `1`, then output will be a multi-line string.
        - If `2`, then output will be a more complex multi-line string with
            additional data.

    Returns
    -
    - `str`
        - String representation of the given object.
    '''

    # validate `lvl`
    if lvl not in [0, 1, 2]:
        raise ValueError(
            f'Invalid {lvl} value: {lvl}, expected value from {{0, 1, 2}}'
        )
        
    # initialize variables
    output: str = '' # string being produced

    # identify datatype
    if obj is None: # none type
        output = str(obj)
    elif isinstance(obj, type): # object type
        output = obj.__name__
    elif isinstance(obj, int): # integer
        output = str(obj)
    elif isinstance(obj, float): # float
        output = str(obj)
    elif isinstance(obj, complex): # complex number
        output = str(obj)
    elif isinstance(obj, str): # string
        if lvl == 0: output = f'"{obj}"'
        elif lvl in [1, 2]:
            output = f'"\n\t\t' + obj.replace('\n', '\n\t\t') + '\n\t"'
    elif isinstance(obj, bool): # boolean
        output = str(obj)
    elif isinstance(obj, dict): # dictionary
        if lvl == 0: output = str(obj)
        elif lvl in [1, 2]:
            output = (
                'dict(\n\t\t' \
                + ',\n\t\t'.join(
                    (
                        f'#{i} {key}: ' \
                        + to_str(val, lvl - 1).replace('\n', '\n\t')
                    )
                    for i, (key, val) in enumerate(obj.items())
                )
                + '\n\t}'
            )
    elif isinstance(obj, ( # sequence data types
            bytes,
            bytearray,
            memoryview,
            list,
            tuple,
            set,
            frozenset,
    )):
        if lvl == 0: output = ','.join([str(x) for x in obj])
        elif lvl == 1:
            output = (
                f'{obj.__class__.__name__}(\n\t\t' \
                + ',\n\t\t'.join([
                    f'{i}: {str(x)}'
                    for i, x in enumerate(list(obj)[:20])
                ])
            )
            if len(obj) > 20: output += f',\n\t\t... + {len(obj) - 20} items'
            output += '\n\t)'
        else:
            output = (
                f'{obj.__class__.__name__}(\n\t\t' \
                + ',\n\t\t'.join([
                    f'#{i}: ' + to_str(x, 1).replace('\n', '\n\t')
                    for i, x in enumerate(obj)
                ]) \
                + '\n\t)'
            )
    elif isinstance(obj, range): # range object
        output = str(obj)
    elif callable(obj): # function
        output = obj.__name__
    elif isinstance(obj, OBJ): # custom object
        if lvl in [1, 2]: output = str(obj)
        else: output = repr(obj)
    else: # unknown object type
        if lvl in [0, 1]: output = f'Unknown Object Type: {obj}'
        elif lvl == 2: output = f'Unknown Object Type: {obj!r}'

    # single-line output additional editing
    if lvl == 0:
        # prevent multiple lines
        output = output.replace('\n', '< NEWLINE />')

        # cap length at 100 characters
        if (len(output) > 100):
            output = f'{output[:97]}... + {len(output) - 97}'

    return output


# =============================================================================
# Base Object Definition
# =============================================================================
class OBJ(object):
    '''
    Base Object
    -
    Represents a base object with generic functionality that all other objects
    can inherit from.

    Custom Attributes
    -
    None

    Custom Constants
    -
    - _DATA : `Type`
        - Collection of data from an object.

    Custom Methods
    -
    - __call__(*args, **kwargs) : `Any`
        - Instance Method.
        - Runs when the current object is called as a function.
    - __del__() : `None`
        - Instance Method.
        - Called after the object's garbage collection has occurred (once all
            references to the object have been destroyed).
    - __enter__() : `OBJ`
        - Instance Method.
        - Called when execution enters the context of the `with` statement.
    - __eq__(other) : `bool`
        - Instance Method.
        - Used to check if the current object is equal to another object.
    - __exit__(exc_type, exc_value, exc_tb) : `None`
        - Instance Method.
        - Called when execution leaves the context of the `with` statement.
    - __gt__(other) : `bool`
        - Instance Method.
        - Used to check if the current object is greater than another object.
    - __hash__() : `int`
        - Instance Method.
        - Used to calculate the hash value of the current object.
    - __html__() : `str`
        - Instance Method.
        - Creates a HTML representation of the current object.
    - __init__(*args, **kwargs) : `None`
        - Instance Method.
        - Used to construct a new instance of the object.
    - __repr__() : `str`
        - Instance Method.
        - Creates a multiple line string representation of the current object.
    - __str__() : `str`
        - Instance Method.
        - Creates a single line string representation of the current object.
    - _get_data(lvl=0) : `dict[str, Any]`
        - Instance Method.
        - Produces a `dict` of keys and values of the data from the object.
    - debug(indent=0) : `str`
        - Instance Method.
        - Produces a multiple line string containing all of the current data
            from the object.
    - duplicate() : `OBJ`
        - Instance Method.
        - Creates an exact duplicate of the current object, without shared
            object references.

    Custom Properties
    -
    None
    '''

    # =========
    # Constants
    _DATA = Dict[str, Any]
    ''' Collection of data from an object. '''

    # =============
    # Instance Call
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        '''
        Instance Call
        -
        Runs when the current object is called as a function.

        Parameters
        -
        - *args : `Any`
            - Positional arguments to the current object instance call.
        - **kwargs : `Any`
            - Keyword arguments to the current object instance call.

        Returns
        -
        - `Any`
            - Return value of the current object instance call.
        '''

        raise NotImplementedError(
            f'OBJ().__call__(*args = {args}, **kwargs = {kwargs}) not ' \
            + f'defined in {self.__class__.__name__}.'
        )

    # ==========
    # Destructor
    def __del__(self) -> None:
        '''
        Destructor
        -
        Called after the object's garbage collection has occurred (once all
        references to the object have been destroyed).

        Parameters
        -
        None

        Returns
        -
        None
        '''

        return None
    
    # ===========
    # Entry Point
    def __enter__(self) -> 'OBJ':
        '''
        Entry Point
        -
        Called when execution enters the context of the `with` statement.

        Parameters
        -
        None

        Returns
        -
        - `OBJ`
            - Object the `with` statement was implemented on.
        '''

        return self

    # ==============
    # Equality Check
    def __eq__(self, other: Any) -> bool:
        '''
        Equality Check
        -
        Used to check if the current object is equal to another object.

        Parameters
        -
        - other : `Any`
            - Other object being compared against this object.

        Returns
        -
        - `bool`
            - Whether or not the current object is equal to the other object.
        '''

        raise NotImplementedError(
            f'OBJ.__eq__(other = {other}) not defined in ' \
            + f'{self.__class__.__name__}.'
        )
    
    # ==========
    # Exit Point
    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> None:
        '''
        Exit Point
        -
        Called when execution leaves the context of the `with` statement.

        Parameters
        -
        - exc_type : `Type[BaseException] | None`
            - `None` if no exception was raised.
            - Type of exception that was raised during execution.
        - exc_val : `BaseException | None`
            - `None` if no exception was raised.
            - Exception that was raised during execution.
        - exc_tb : `TracebackType | None`
            - `None` if no exception was raised.
            - Traceback of the exception that was raised during execution.

        Returns
        -
        None
        '''

        return None
    
    # ================
    # Inequality Check
    def __gt__(self, other: Any) -> bool:
        '''
        Inequality Check
        -
        Used to check if the current object is greater than another object.

        Parameters
        -
        - other : `Any`
            - Other object being compared against this object.

        Returns
        -
        - `bool`
            - Whether or not the current object is greater than the other   
                object.
        '''

        raise NotImplementedError(
            f'OBJ.__gt__(other = {other}) not defined in ' \
            + f'{self.__class__.__name__}.'
        )
    
    # =============
    # Generate Hash
    def __hash__(self) -> int:
        '''
        Generate Hash
        -
        Used to calculate the hash value of the current object.

        Parameters
        -
        None

        Returns
        -
        - `int`
            - Hash value of the current object.
        '''

        raise NotImplementedError(
            f'OBJ.__hash__() not defined in {self.__class__.__name__}.'
        )
    
    # ===============
    # Get Object HTML
    def __html__(self) -> str:
        '''
        Get Object HTML
        -
        Creates a HTML representation of the current object.

        Parameters
        -
        None

        Returns
        -
        - `str`
            - HTML representation of the current object.
        '''

        raise NotImplementedError(
            f'OBJ.__html__() not defined in {self.__class__.__name__}.'
        )
    
    # ===========
    # Constructor
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        '''
        Constructor
        -
        Used to construct a new instance of the object.

        Parameters
        -
        - *args : `Any`
            - Positional arguments to pass to the constructor of the subclass.
        - **kwargs : `Any`
            - Keyword arguments to pass to the constructor of the subclass.

        Returns
        -
        None
        '''

        raise NotImplementedError(
            f'OBJ.__init__(*args = {args}, **kwargs = {kwargs}) not defined ' \
            + f'in {self.__class__.__name__}.'
        )

    # ===================================
    # Multiple Line String Representation
    def __repr__(self) -> str:
        '''
        Multiple Line String Representation
        -
        Creates a multiple line string representation of the current object.

        Parameters
        -
        None

        Returns
        -
        - `str`
            - Multiple line string representation of the current object.
        '''

        return (
            f'<{self.__class__.__name__}\n\t' \
            + ',\n\t'.join([
                f'{key} = ' + to_str(val, lvl = 1).replace('\n', '\n\t')
                for key, val in self._get_data(1).items()
            ]) \
            + f'\n/{self.__class__.__name__}>'
        )
    
    # =================================
    # Single Line String Representation
    def __str__(self) -> str:
        '''
        Single Line String Representation
        -
        Creates a single line string representation of the current object.

        Parameters
        -
        None

        Returns
        -
        - `str`
            - Single line string representation of the current object.
        '''

        return (
            f'{self.__class__.__name__} ' \
            + ', '.join([
                f'{key} = {to_str(val, lvl = 0)}'
                for key, val in self._get_data(0).items()
            ])
        )

    # ===============
    # Get Object Data
    def _get_data(self, lvl: int = 0) -> _DATA:
        '''
        Get Object Data
        -
        Produces a `dict` of keys and values of the data from the object.

        Parameters
        -
        - lvl : `int`
            - Defaults to `0`, meaning that only the key data values (typically
                1 - 3 data points) will be returned. Implemented by `__str__`
                to get a single line string representation of the object.
            - If `1`, then returns a more in-depth set of data. Implemented by
                `__repr__` to get a multi line string representation of the
                object.
            - If `2`, then returns an extremely in-depth set of data containing
                everything stored in the object. Used for the purposes of
                debugging.

        Returns
        -
        - `OBJ._DATA`
            - Collection of data from the object instance.
        '''

        # validate `lvl`
        if lvl not in [0, 1, 2]:
            raise ValueError(
                f'Invalid {lvl} value: {lvl}, expected value from {{0, 1, 2}}'
            )
        
        # return empty data set
        return {}
    
    # ============
    # Debug Object
    def debug(self, indent: int = 0) -> str:
        '''
        Debug Object
        -
        Produces a multiple line string containing all of the current data from
        the object.

        Parameters
        -
        - indent : `int`
            - Number of tabs to indent each internal string of the multiple
                line output by.
            - Defaults to `0`, meaning that no indentation will occur.

        Returns
        -
        - `str`
            - Multiple line string containing all of the debug information from
                the current object.
        '''

        # calculate additional indentation
        t: str = '\t' * indent

        return (
            f'{t}<{self.__class__.__name__}\n\t{t}' \
            + f',\n\t{t}'.join([
                f'{key} = ' + to_str(val, lvl = 2).replace('\n', f'\n\t{t}')
                for key, val in self._get_data(2).items()
            ]) \
            + f',\n{t}/{self.__class__.__name__}>'
        )
    
    # ================
    # Duplicate Object
    def duplicate(self) -> 'OBJ':
        '''
        Duplicate Object
        -
        Creates an exact duplicate of the current object, without shared object
        references.

        Parameters
        -
        None

        Returns
        -
        - `OBJ`
            - Duplicate of the current object.
        '''

        raise NotImplementedError(
            f'OBJ.duplicate() not defined in {self.__class__.__name__}.'
        )
    

# =============================================================================
# End of File
# =============================================================================
