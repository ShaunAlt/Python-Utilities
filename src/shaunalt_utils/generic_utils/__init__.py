# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Generic Objects
-
Contains a collection of the generic objects and methods that all other parts
of this package implement.

Contents
-
- `logs`
    - Contains the definitions for implementing loggers within projects.
- `obj`
    - Contains the definition for the base object that all other objects can
        inherit from.
- `timer`
    - Contains the definition for the timer object that is used for timing
        sections of code.

Dependencies
-
- `__future__`
    - Used for string type hints.
    - Builtin.
- `concurrent_log_handler`
    - Used for creating a rotating file handler.
    - `concurrent-log-handler==0.9.25`
- `logging`
    - Used for creating / getting loggers.
    - Builtin.
- `time`
    - Used for timing functionality.
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

# logger creation
from .logs import get_logger

# base object
from .obj import OBJ

# timer object
from .timer import TIMER


# =============================================================================
# End of File
# =============================================================================
