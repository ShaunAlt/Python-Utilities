# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Forms
-
Contains a collection of methods and objects that can be used for creating form
fields, manipulating and validating data, and generating forms.

Contents
-
- `generator`
    - Contains the method used for dynamically creating form fields.
TODO: Fix this
- create field.
- validate field.
- single select field fde.
- multi select field fde.
- base form.

Dependencies
-
- `flask_wtf`
    - Used for the base flask form model used for creating all forms.
    - `flask-wtf==1.2.1`.
- `typing`
    - Used for type hinting.
    - Builtin.
- `wtforms`
    - Used for type hinting and creating the form fields.
    - `wtforms==3.1.2`.

Internal Dependencies
-
None
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

# field generator
from .generator import (
    create_field, # dynamically create form fields
)


# =============================================================================
# End of File
# =============================================================================
