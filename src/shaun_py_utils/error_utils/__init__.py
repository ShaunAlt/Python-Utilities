# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Errors
-
Contains a collection of methods and objects that can be used for simplifying
the process of handling and reporting errors.

Contents
-
- `handler_default`
    - Contains the method that can be used to simplify the handling of errors.

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

# used for default error handling
from .handler_default import error_handler


# =============================================================================
# End of File
# =============================================================================
