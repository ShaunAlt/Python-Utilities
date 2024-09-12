# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Emails
-
Contains a collection of methods and objects used to simplify the process of
creating and sending emails.

Contents
-
- `errors`
    - Contains the definitions of the custom errors that are implemented in
        this sub-module.
- `model`
    - Contains the definition of the main email object that stores all of the
        information required to create a new email message.

Dependencies
-
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

# email mode
from .model import Email


# =============================================================================
# End of File
# =============================================================================
