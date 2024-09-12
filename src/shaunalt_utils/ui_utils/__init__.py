# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - User Interface
-
Contains a collection of objects and methods that can be used for simplifying
the dynamic creation of templated user interfaces.

Contents
-
- `nav`
    - Contains the objects that can be used to create a dynamic navigation
        menu.
- `page`
    - Contains the objects that can be used to create a dynamic web-page.
- `table`
    - Contains the objects that can be used to create a dynamic table.

Dependencies
-
- `__future__`
    - Used for string type hints.
    - Builtin.
- `datetime`
    - Used for getting date/time.
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

# navigation menu objects
from .nav import (
    UI_Nav_OBJ, # generic navigation object
    UI_Nav_Button, # individual button in the navigation menu
    UI_Nav_Dropdown, # dropdown menu containing child `Nav_OBJ` objects
)

# page objects
from .page import (
    UI_Page, # page object
)

# table objects
from .table import (
    UI_Table, # main table
    UI_Table_Btns, # table buttons
    UI_Table_Row, # table row
)


# =============================================================================
# End of File
# =============================================================================
