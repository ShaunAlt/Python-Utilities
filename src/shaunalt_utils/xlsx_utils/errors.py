# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - XLSX - Custom Errors
-
Contains the definitions of the custom errors that are implemented in this
sub-module.

Contents
-
- `PreExistingColumnID`
    - Exception raised when a new header column is being added to an xlsx
        sheet, but the new id already exists in that sheet.

Dependencies
-
None

Internal Dependencies
-
None
'''
# =============================================================================


# =============================================================================
# Pre-Existing Column ID
# =============================================================================
class PreExistingColumnID(Exception):
    '''
    Exception raised when a new header column is being added to an xlsx sheet,
    but the new id already exists in that sheet.
    '''


# =============================================================================
# End of File
# =============================================================================
