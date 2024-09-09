# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - User Interface - Navigation Menu
-
Contains the objects that can be used to create a dynamic navigation menu.

Contents
-
- `Nav_Button`
    - Individual button in the navigation menu that can be used to go to a
        specific route.
- `Nav_Dropdown`
    - Dropdown menu that can be used to display a list of options in the
        navigation menu.
    
Dependencies
-
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

# used for base object definition
from ..generic_utils import OBJ

# used for type hinting
from typing import (
    Any, # any type
    List, # list type
    Type, # type of object type
)


# =============================================================================
# Navigation Button Definition
# =============================================================================
class Nav_Button(OBJ):
    '''
    Navigation Button
    -
    Individual button in the navigation menu that can be used to go to a
    specific route.

    Custom Attributes
    -
    - _borders : `str | None`
        - Optional string, defaulting to `None`, indicating no borders should
            be displayed on the button. If not `None` or an empty string,
            borders should be displayed on the button depending on if the
            required characters are present in this string.
        - `"T" | "t"` - Include the TOP border.
        - `"B" | "b"` - Include the BOTTOM border.
        - `"L" | "l"` - Include the LEFT border.
        - `"R" | "r"` - Include the RIGHT border.
    - _confirm : `str | None`
        - Defaults to `None`. If not `None` or an empty string, then upon
            being clicked, this navigation button will create a javascript
            "confirm" box with the provided text inside it, requested
            confirmation from the user before going to the given route.
    - _count : `int | None`
        - Defaults to `None`, indicating no warning number should be displayed
            on this button. If not `None`, a small warning badge will be
            created in the corner of this navigation button, which could be
            used to indicate a count of something.
    - _icon : `str | None`
        - Defaults to `None`, meaning no icon will be created for that
            particular navigation button. If set, then creates an `<i>` html
            element with the icon name in the class. See FontAwesome.com for
            more details.
    - _label : `str`
        - Text to display on the button.
    - _route : `str`
        - `flask.url_for` output (or equivalent if implementing a different
            framework), which indicates the route to go to if this button is
            clicked.
    - _tooltip : `str | None`
        - Defaults to `None`, indicating this button doesn't have a tooltip.
            If not an empty string, will create a tooltip for this button.

    Custom Constraints
    -
    None

    Custom Methods
    -
    - __init__(...) : `None`
        - Instance Method.
        - Creates a new navigation button.
    - _get_data(lvl=0) : `OBJ._DATA`
        - `OBJ` Instance Method.
        - Produces a `dict` of keys and values of the data from the object.

    Custom Properties
    -
    None
    '''

    import markupsafe


# =============================================================================
# Navigation Dropdown Definition
# =============================================================================


# =============================================================================
# End of File
# =============================================================================
