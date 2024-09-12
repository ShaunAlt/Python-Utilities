# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Emails - Custom Errors
-
Contains the definitions of the custom errors that are implemented in this
sub-module.

Contents
-
- `InvalidAttachmentError`
    - Exception raised when an unsupported file type is encountered when trying
        to add an attachment to an email.

Dependencies
-
None

Internal Dependencies
-
None
'''
# =============================================================================


# =============================================================================
# Invalid Attachment File Type
# =============================================================================
class InvalidAttachmentError(Exception):
    '''
    Exception raised when an unsupported file type is encountered when trying
    to add an attachment to an email.
    '''


# =============================================================================
# End of File
# =============================================================================
