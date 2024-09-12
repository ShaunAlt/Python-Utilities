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
- `errors`
    - Contains the definitions of the custom errors that are implemented in
        this sub-module.
- `nav`
    - Contains the objects that can be used to create a dynamic navigation
        menu.
- `table`
    - Contains the objects that can be used to create a dynamic table.
TODO: Fix this
- Page
- Table/Row/Btns/Desc.
- Nav Btn/Dropdown/Section.
- return_page
- UI_Button.
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

# table objects
from .table import (
    UI_Table, # main table
    UI_Table_Btns, # table buttons
    UI_Table_Row, # table row
)


# =============================================================================
# End of File
# =============================================================================
