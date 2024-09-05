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
    - Contains a collections of methods that can be used as decorators for
        functions.
- `email_utils`
    - Contains a collection of methods and objects that can be used to simplify
        the process of creating and sending emails.
- `error_utils`
    - Contains a collection of methods and objects that can be used for
        simplifying the process of handling and reporting errors.
- `flask_utils`
    - Contains a collection of methods used for simplifying the implementation
        of the Flask web framework for building web applications.
- `form_utils`
    - Contains a collection of methods and objects that can be used for
        creating form fields, manipulating and validating data, and generating
        forms.
- `generic_utils`
    - Contains a collection of generic objects and methods that all other parts
        of this package implement.
- `sqlalchemy_utils`
    - Contains a collection of methods and objects that can be used for
        simplifying the implementation of the SQLAlchemy package for working
        with databases.
- `ui_utils`
    - Contains a collection of objects and methods that can be used for
        simplifying the dynamic creation of templated user interfaces.
- `xlsx_utils`
    - Contains a collection of methods that can be used for creating and
        editing data in an XLSX document.
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
