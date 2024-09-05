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

Dependencies
-
- `__future__`
    - Used for string type hints.
    - Builtin.
- `concurrent_log_handler`
    - Used for creating a rotating file handler.
    - `concurrent-log-handler==0.9.25`
- `email`
    - Used for creating email messages.
    - Builtin.
- `io`
    - Used for storing raw file content.
    - Builtin.
- `logging`
    - Used for creating / getting loggers.
    - Builtin.
- `mimetypes`
    - Used for creating mimetypes for common file types.
    - Builtin.
- `smtplib`
    - Used for connecting to the SMTP server.
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
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

# decorator objects + methods
# from .decorator_utils import (

# )

# email objects + methods
from .email_utils import (
    Email, # email model
)

# error objects + methods
# from .error_utils import (

# )

# flask objects + methods
# from .flask_utils import (
    
# )

# form objects + methods
# from .form_utils import (

# )

# generic objects + methods
from .generic_utils import (
    get_logger, # get / create module logger
    OBJ, # generic base object
    TIMER, # timer object
)

# sqlalchemy objects + methods
# from .sqlalchemy_utils import (

# )

# ui objects + methods
# from .ui_utils import (

# )

# xlsx objects + methods
# from .xlsx_utils import (

# )


# =============================================================================
# End of File
# =============================================================================
