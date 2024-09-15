# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Generic - Timer Object
-
Contains the definition for the timer object that is used for timing sections
of code.

Contents
-
- `TIMER`
    - Used for timing sections of code - measuring elapsed time with
        `perf_counter_ns`.
    
Dependencies
-
- `logging`
    - Used for creating / getting loggers.
    - Builtin.
- `time`
    - Used for timing functionality.
    - Builtin.
- `typing`
    - Used for type hinting.
    - Builtin.

Internal Dependencies
-
- `.obj`
    - Used for base object definition.
    - `generic_utils.obj`.

Future Versions
-
- Instead of always using the `perf_counter_ns` function, users should be able
    to parse their own function that the `TIMER` instance would implement
    instead.
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

# used for base object definition
from .obj import OBJ

# used for logging data
import logging

# used for timing functionality
from time import perf_counter_ns

# used for type-hinting
from typing import (
    Any, # any type
    Dict, # dictionary type
)


# =============================================================================
# Timer Object Definition
# =============================================================================
class TIMER(OBJ):
    '''
    Timer Object
    -
    Used for timing sections of code - measuring elapsed time with
    `perf_counter_ns`.

    Custom Attributes
    -
    - _logger : `logging.Logger`
        - Logger used for logging all of the timing information to a timing log
            file.
    - _lvl : `int`
        - Verbosity indentation level.
        - Defaults to `-1`, meaning that none of the timing information will be
            logged.
        - Any value `0` or greater will result in the timing information being
            logged with `_lvl` tabs used to indent each message (indents used
            to simplify pretty-printing).
    - _name : `str`
        - Name of the module, class, and/or method that the `TIMER` has been
            implemented in.
    - _start : `int`
        - Start time for the timer.

    Custom Constants
    -
    None

    Custom Methods
    -
    - __del__() : `None`
        - `OBJ` Instance Method.
        - Called after the object's garbage collection has occurred (once all
            references to the object have been destroyed).
    - __init__(name, logger, lvl=-1) : `None`
        - Instance Method.
        - Initializes the timer object.
    - _get_data(lvl=0) : `_OBJ.DATA`
        - `OBJ` Instance Method.
        - Produces a `dict` of keys and values of the data from the object.
    - get_sub(indent=1) : `int`
        - Instance Method.
        - Calculates the verbosity indentation level for a timer called within
            the current timer.
    - lap(name, indent=0) : `TIMER`
        - Instance Method.
        - Creates a sub-timer which is used to time a specified section of code
            within the current timer.
    - log(msg, lvl=logging.DEBUG, indent=0, prefix='| - ') : `None`
        - Instance Method.
        - Logs the given message to the timing log file.
    - stop(indent=0) : `int`
        - Instance Method.
        - Logs a string of the time elapsed since the creation of the timer.

    Custom Properties
    -
    None

    Implementation Example 1
    -
    >>> t = TIMER(...)
    ...
    >>> with t.lap("Test A"):
    >>>     with t.lap("Test B", 1):
    >>>         with t.lap("Test C", 2):
    >>>             print("Hello World!")
    >>>         with t.lap("Test D", 2):
    >>>             print("Another Print")
    >>> t.stop()
    ...
    (log file) | - Test A
    (log file) |   | - Test B
    (log file) |   |   | - Test C
    Hello World!
    (log file) |   |   |   | - Elapsed Time: XXX (Test C)
    (log file) |   |   | - Test D
    Another Print
    (log file) |   |   |   | - Elapsed Time: XXX (Test D)
    (log file) |   |   | - Elapsed Time: XXX (Test B)
    (log file) |   | - Elapsed Time: XXX (Test A)
    (log file) | - Elapsed Time: XXX

    Implementation Example 2
    -
    >>> def main():
    >>>     t = TIMER("Test Timer")
    ...
    >>>     with t.lap("Test A"):
    >>>         with t.lap("Test B", 1):
    >>>             print("Hello World!")
    >>>         with t.lap("Test C", 1):
    >>>             print("Another Print")
    ...
    >>> main()
    ...
    (log file) | - Test Timer
    (log file) | - Test A
    (log file) |   | - Test B
    Hello World!
    (log file) |   |   | - Elapsed Time: XXX (Test B)
    (log file) |   | - Test C
    Another Print
    (log file) |   |   | - Elapsed Time: XXX (Test C)
    (log file) |   | - Elapsed Time: XXX (Test A)
    (log file) | - Elapsed Time: XXX (Test Timer)
    '''

    # ==========
    # Destructor
    def __del__(self) -> None:
        # whenever the function this timer was created in is finished, or when
        # the `with` statement that this timer was created for is finished, the
        # garbage collection will trigger this. By doing this, it means that
        # the `__exit__` function doesn't need to be modified.
        self.stop(1)
    
    # ===========
    # Constructor
    def __init__(
            self,
            name: str,
            logger: logging.Logger,
            lvl: int = -1
    ) -> None:
        # set object logger
        self._logger: logging.Logger = logger
        ''' Logger used for logging all of the timing information to a timing
            log file. '''
        
        # set verbosity level
        self._lvl: int = lvl
        ''' Verbosity indentation level. Defaults to `-1`, meaning that none of
            the timing information will be logged. Any value `0` or greater
            will result in the timing information being logged with `_lvl` tabs
            used to indent each message (indents used to simplify
            pretty-printing). '''
        
        # set name of the module, class, and/or method
        self._name: str = name
        ''' Name of the module, class, and/or method that the `TIMER` has been
            implemented in. '''
        
        # set start time
        self._start: int = perf_counter_ns()
        ''' Start time for the timer. '''

        # log the creation of the timer
        self.log(self._name)

    # =============
    # OBJ: Get Data
    def _get_data(self, lvl: int = 0) -> OBJ._DATA:
        # initialize data
        data = super()._get_data(lvl)

        # short representation
        if lvl == 0:
            data = {
                'name': self._name,
                'lvl': self._lvl,
                'start': self._start,
            }

        # long representation
        elif lvl in [1, 2]:
            data = {
                'logger': self._logger,
                'lvl': self._lvl,
                'name': self._name,
                'start': self._start,
            }

        return data

    # =======================
    # Get Sub-Timer Verbosity
    def get_sub(self, indent: int = 1) -> int:
        '''
        Get Sub-Timer Verbosity
        -
        Calculates the verbosity indentation level for a timer called within
        the current timer.

        Parameters
        -
        - indent : `int`
            - Amount to increase the indentation by.
            - Defaults to `1`, meaning that one tab will be added to the
                current indentation level. If the current indentation level is
                `-1`, then the new value will stay at `-1`.

        Returns
        -
        - `int`
            - Verbosity indentation level for the sub timer.
        '''

        if self._lvl > -1: return self._lvl + indent
        return -1
    
    # ================
    # Create Lap Timer
    def lap(self, name: str, indent: int = 0) -> 'TIMER':
        '''
        Create Lap Timer
        -
        Creates a sub-timer which is used to time a specified section of code
        within the current timer.

        Parameters
        -
        - name : `str`
            - Name for the new timer.
        - indent : `int`
            - Amount to increase the indentation by. Defaults to `0`.

        Returns
        -
        - `TIMER`
            - Timer used to time a particular sub-section of code.
        '''

        return TIMER(name, self._logger, self.get_sub(indent))
    
    # ===========
    # Log Message
    def log(
            self,
            msg: str,
            lvl: int = logging.DEBUG,
            indent: int = 0,
            prefix: str = '| - '
    ) -> None:
        '''
        Log Message
        -
        Logs the given message to the timing log file.

        Parameters
        -
        - msg : `str`
            - Message to log.
        - lvl : `int`
            - Logging level to write the message with. Defaults to
                `logging.DEBUG`.
        - indent : `int`
            - Amount of additional indentation levels to use when writing the
                message. Defaults to `0`.
        - prefix : `str`
            - Defaults to `"| - "`, which is prefixed to the start of the log
                message. Used purely for improving the readability of the log
                messages.

        Returns
        -
        None
        '''

        if self._lvl > -1:
            indent_str = '|\t' * (self._lvl + indent)
            self._logger.log(lvl, f'{indent_str}{prefix}{msg}')

    # ==========
    # Stop Timer
    def stop(self, indent: int = 0) -> int:
        '''
        Stop Timer
        -
        Logs a string of the time elapsed since the creation of the timer.

        Parameters
        -
        - indent : `int`
            - Amount of additional indentation levels to use when writing the
                log message. Defaults to `0`.

        Returns
        -
        - `int`
            - Number of nanoseconds elapsed since the creation of the timer.
        '''

        # get elapsed time
        diff: int = perf_counter_ns() - self._start

        # log elapsed time
        # - converts from nanoseconds (1e-9) to milliseconds (1e-3)
        # - output contains 3 decimal places, and uses commas to denote the
        #   thousands, millions, etc.
        # - Example String: "Elapsed Time: 1,234,567.890 ms (Example Timer)"
        self.log(
            f'Elapsed Time: {(diff / 1e6):,.3f} ms ({self._name})',
            indent = indent
        )

        # return elapsed time
        return diff


# =============================================================================
# End of File
# =============================================================================
