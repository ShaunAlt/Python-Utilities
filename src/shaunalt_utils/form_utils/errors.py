# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Forms - Custom Errors
-
Contains the definitions of the custom errors that are implemented in this
sub-module.

Contents
-
- `FieldTypeError`
    - Exception raised when a new field is being created but the type of field
        that was told to be created does not exist.

Dependencies
-
None

Internal Dependencies
-
None
'''
# =============================================================================


# =============================================================================
# Field Type Error
# =============================================================================
class FieldTypeError(Exception):
    '''
    Exception raised when a new field is being created but the type of field
    that was told to be created does not exist.
    '''


# =============================================================================
# End of File
# =============================================================================
