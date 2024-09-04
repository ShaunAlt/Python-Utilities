# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities
-
Contains a collection of objects and methods that can be used to simplify
processes in various applications.

Contents
-
- `decorator_utils`
    - N/A.
- `email_utils`
    - N/A.
- `error_utils`
    - N/A.
- `flask_utils`
    - N/A.
- `form_utils`
    - N/A.
- `generic_utils`
    - Contains a collection of generic objects and methods that all other parts
        of this package implement.
- `sqlalchemy_utils`
    - N/A.
- `ui_utils`
    - N/A.
- `xlsx_utils`
    - N/A.
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

# generic objects
from .generic_utils import (
    get_logger, # get / create module logger
    OBJ, # generic base object
    TIMER, # timer object
)


# =============================================================================
# End of File
# =============================================================================
