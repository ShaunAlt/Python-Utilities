# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - User Interface - Navigation Menu
-
Contains the objects that can be used to create a dynamic navigation menu.

Contents
-
- `UI_Nav_OBJ`
    - Base class for navigation objects, containing key shared functionality.
- `UI_Nav_Button`
    - Individual button in the navigation menu that can be used to go to a
        specific route.
- `UI_Nav_Dropdown`
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
    List, # list type
    Optional, # optional type
)


# =============================================================================
# Generic Navigation Object Definition
# =============================================================================
class UI_Nav_OBJ(OBJ):
    '''
    Generic Navigation Object
    -
    Base class for navigation objects, containing key shared functionality.

    Custom Attributes
    -
    - _border_bottom : `bool`
        - Whether or not a border should be displayed at the bottom of the
            navigation element.
    - _border_left : `bool`
        - Whether or not a border should be displayed at the left of the
            navigation element.
    - _border_right : `bool`
        - Whether or not a border should be displayed at the right of the
            navigation element.
    - _border_top : `bool`
        - Whether or not a border should be displayed at the top of the
            navigation element.
    - _confirm : `str | None`
        - Defaults to `None`. If not `None` or an empty string, then when the
            navigation element is clicked, it will generate a JavaScript
            confirmation alert box with the provided text inside. 
    - _count : `int | None`
        - Defaults to `None`, indicating no warning number should be displayed
            on this navigation element. If not `None`, a small warning badge
            will be created in the corner of this navigation element, which
            could be used to indicate a count of something.
    - _current : `bool`
        - Defaults to `False`, meaning that the navigation element is not
            formatted differently. If `True`, this indicates that the
            navigation element should be highlighted to indicate that it has
            been used to select the current page.
    - _icon : `str | None`
        - Defaults to `None`, meaning no icon will be created for that
            particular navigation element. If set, then creates an `<i>` html
            element with the icon name in the class. See FontAwesome.com for
            more details.
    - _label : `str`
        - Text to display on the navigation element.
    - _route : `str | None`
        - `flask.url_for` output (or equivalent if implementing a different
            framework), which indicates the route to go to if this navigation
            element is clicked.
    - _tooltip : `str | None`
        - Defaults to `None`, indicating this navigation element doesn't have a
            tooltip. If not an empty string, will create a tooltip for this
            navigation element.

    Custom Constants
    -
    None

    Custom Methods
    -
    - __init__(label, ...) : `None`
        - Instance Method.
        - Creates a new navigation element.
    - _get_data(lvl=0) : `OBJ._DATA`
        - `OBJ` Instance Method.
        - Produces a `dict` of keys and values of the data from the object.

    Custom Properties
    -
    - border_bottom : `bool`
        - Whether or not a border should be displayed below the navigation
            element.
    - border_left : `bool`
        - Whether or not a border should be displayed left of the navigation
            element.
    - border_right : `bool`
        - Whether or not a border should be displayed right of the navigation
            element.
    - border_top : `bool`
        - Whether or not a border should be displayed above the navigation
            element.
    - borders : `str`
        - String indicating which borders should be displayed.
    - confirm : `str | None`
        - String containing a confirmation message. If `None` then no message
            will be displayed.
    - count : `int | None`
        - Notification number for the navigation element. If `None` then no
            number will be displayed.
    - current : `bool`
        - Whether or not the navigation element is for the current page.
    - icon : `str | None`
        - FontAwesome icon to display. If `None` then no icon will be shown.
    - label : `str`
        - Label text to display on the navigation element.
    - route : `str | None`
        - Route to create a "GET" request for when this navigation element is
            clicked.
    - tooltip : `str | None`
        - Navigation element tooltip text. If `None` then no tooltip will be
            shown.
    - visible : `bool`
        - Flag used to indicate whether or not the navigation element should be
            rendered in the html template.
    '''

    # ===========
    # Constructor
    def __init__(
            self,
            label: str,
            route: Optional[str] = None,
            current: bool = False,
            icon: Optional[str] = None,
            count: Optional[int] = None,
            border_top: bool = False,
            border_right: bool = False,
            border_bottom: bool = False,
            border_left: bool = False,
            tooltip: Optional[str] = None,
            confirm: Optional[str] = None
    ) -> None:
        # set borders
        self._border_bottom: bool = border_bottom
        ''' Whether or not a border should be displayed at the bottom of the
            navigation element. '''
        self._border_left: bool = border_left
        ''' Whether or not a border should be displayed at the left of the
            navigation element. '''
        self._border_right: bool = border_right
        ''' Whether or not a border should be displayed at the right of the
            navigation element. '''
        self._border_top: bool = border_top
        ''' Whether or not a border should be displayed at the top of the
            navigation element. '''

        # set confirmation message
        self._confirm: Optional[str] = confirm
        ''' Defaults to `None`. If not `None` or an empty string, then when the
            navigation element is clicked, it will generate a JavaScript
            confirmation alert box with the provided text inside. '''

        # set count notification
        self._count: Optional[int] = count
        ''' Defaults to `None`, indicating no warning number should be
            displayed on this navigation element. If not `None`, a small
            warning badge will be created in the corner of this navigation
            element, which could be used to indicate a count of something. '''

        # set current page indicator
        self._current: bool = current
        ''' Defaults to `False`, meaning that the navigation element is not
            formatted differently. If `True`, this indicates that the
            navigation element should be highlighted to indicate that it has
            been used to select the current page. '''

        # set icon
        self._icon: Optional[str] = icon
        ''' Defaults to `None`, meaning no icon will be created for that
            particular navigation element. If set, then creates an `<i>` html
            element with the icon name in the class. See FontAwesome.com for
            more details. '''

        # set label
        self._label: str = label
        ''' Test to display on the navigation element. '''

        # set current page indicator
        self._route: Optional[str] = route
        ''' `flask.url_for` output (or equivalent if implementing a different
            framework), which indicates the route to go to if this navigation
            element is clicked. '''

        # set tooltip
        self._tooltip: Optional[str] = tooltip
        ''' Defaults to `None`, indicating this navigation element doesn't
            have a tooltip. If not an empty string, will create a tooltip for
            this navigation element. '''

    # ==========================
    # Property - Border - Bottom
    @property
    def border_bottom(self) -> bool:
        ''' Whether or not a border should be displayed below the navigation
            element. '''
        return self._border_bottom
    
    # ========================
    # Property - Border - Left
    @property
    def border_left(self) -> bool:
        ''' Whether or not a border should be displayed left of the navigation
            element. '''
        return self._border_left
    
    # =========================
    # Property - Border - Right
    @property
    def border_right(self) -> bool:
        ''' Whether or not a border should be displayed right of the
            navigation element. '''
        return self._border_right

    # =======================
    # Property - Border - Top
    @property
    def border_top(self) -> bool:
        ''' Whether or not a border should be displayed above the navigation
            element. '''
        return self._border_top

    # =========================
    # Property - Borders String
    @property
    def borders(self) -> str:
        ''' String indicating which borders should be displayed. '''
        return (
            ('B' if self.border_bottom else '')
            + ('L' if self.border_left else '')
            + ('R' if self.border_right else '')
            + ('T' if self.border_top else '')
        )
    
    # ===============================
    # Property - Confirmation Message
    @property
    def confirm(self) -> Optional[str]:
        ''' String containing a confirmation message. If `None` then no message
            will be displayed. '''
        return self._confirm

    # =============================
    # Property - Count Notification
    @property
    def count(self) -> Optional[int]:
        ''' Notification number for the navigation element. If `None` then no
            number will be displayed. '''
        return self._count

    # =================================
    # Property - Current Page Indicator
    @property
    def current(self) -> bool:
        ''' Whether or not the navigation element is for the current page. '''
        return self._current

    # ===============
    # Property - Icon
    @property
    def icon(self) -> Optional[str]:
        ''' FontAwesome icon to display. If `None` then no icon will be
            shown. '''
        return self._icon

    # ================
    # Property - Label
    @property
    def label(self) -> str:
        ''' Label text to display on the navigation element. '''
        return self._label
    
    # ================
    # Property - Route
    @property
    def route(self) -> Optional[str]:
        ''' Route to create a "GET" request for when this navigation element is
            clicked. '''
        return self._route

    # ==================
    # Property - Tooltip
    @property
    def tooltip(self) -> Optional[str]:
        ''' Navigation element tooltip text. If `None` then no tooltip will be
            shown. '''
        return self._tooltip
    
    # ==================
    # Property - Visible
    @property
    def visible(self) -> bool:
        ''' Flag used to indicate whether or not the navigation element should
            be rendered in the html template. '''
        raise NotImplementedError(
            'Nav_OBJ().visible is not implemented in ' \
            + f'{self.__class__.__name__}'
        )
    
    # =============
    # OBJ: Get Data
    def _get_data(self, lvl: int = 0) -> OBJ._DATA:
        # initialize data
        data = super()._get_data(lvl)

        # short representation
        if lvl == 0:
            data['label'] = self.label
            data['route'] = self.route
            data['visible'] = self.visible

        # long representation
        elif lvl == 1:
            data['borders'] = self.borders
            data['confirm'] = self.confirm
            data['count'] = self.count
            data['current'] = self.current
            data['icon'] = self.icon
            data['label'] = self.label
            data['route'] = self.route
            data['tooltip'] = self.tooltip
            data['visible'] = self.visible

        # debug
        elif lvl == 2:
            data['_border_bottom'] = self._border_bottom
            data['_border_left'] = self._border_left
            data['_border_right'] = self._border_right
            data['_border_top'] = self._border_top
            data['_confirm'] = self._confirm
            data['_count'] = self._count
            data['_current'] = self._current
            data['_icon'] = self._icon
            data['_label'] = self._label
            data['_route'] = self._route
            data['_tooltip'] = self._tooltip
            data['border_bottom'] = self.border_bottom
            data['border_left'] = self.border_left
            data['border_right'] = self.border_right
            data['border_top'] = self.border_top
            data['borders'] = self.borders
            data['confirm'] = self.confirm
            data['count'] = self.count
            data['current'] = self.current
            data['icon'] = self.icon
            data['label'] = self.label
            data['route'] = self.route
            data['tooltip'] = self.tooltip
            data['visible'] = self.visible

        return data


# =============================================================================
# Navigation Button Definition
# =============================================================================
class UI_Nav_Button(UI_Nav_OBJ):
    '''
    Navigation Button
    -
    Individual button in the navigation menu that can be used to go to a
    specific route.

    Custom Attributes
    -
    None

    Custom Constants
    -
    None

    Custom Methods
    -
    - __init__(label, route, ...) : `None`
        - Instance Method.
        - Creates a new navigation button.
    - _get_data(lvl=0) : `OBJ._DATA`
        - `OBJ` Instance Method.
        - Produces a `dict` of keys and values of the data from the object.

    Custom Properties
    -
    - route : `str`
        - Route to create a "GET" request for when this button is clicked.
            Typically used to go to a new page in the application.
    - visible : `bool`
        - Flag used to indicate whether or not the navigation element should be
            rendered in the html template.
    '''

    # ===========
    # Constructor
    def __init__(
            self,
            label: str,
            route: str,
            current: bool = False,
            icon: Optional[str] = None,
            count: Optional[int] = None,
            border_top: bool = False,
            border_right: bool = False,
            border_bottom: bool = False,
            border_left: bool = False,
            tooltip: Optional[str] = None,
            confirm: Optional[str] = None
    ) -> None:
        # create base navigation element values
        super().__init__(
            label = label,
            route = route,
            current = current,
            icon = icon,
            count = count,
            border_top = border_top,
            border_right = border_right,
            border_bottom = border_bottom,
            border_left = border_left,
            tooltip = tooltip,
            confirm = confirm
        )

    # ================
    # Property - Route
    @property
    def route(self) -> str:
        ''' Route to create a "GET" request for when this button is clicked.
            Typically used to go to a new page in the application. '''

        # validate route is not empty
        if self._route is None: raise ValueError('Button route is None.')
        return self._route
    
    # ==================
    # Property - Visible
    @property
    def visible(self) -> bool:
        ''' Flag used to indicate whether or not the navigation element should
            be rendered in the html template. '''

        return (
            (self.label != '') # label is not empty
            and (self._route is not None) # route is valid
        )

    # =============
    # OBJ: Get Data
    def _get_data(self, lvl: int = 0) -> OBJ._DATA:
        # initialize data
        data = super()._get_data(lvl)

        return data


# =============================================================================
# Navigation Dropdown Definition
# =============================================================================
class UI_Nav_Dropdown(UI_Nav_OBJ):
    '''
    Navigation Dropdown
    -
    Individual dropdown in the navigation menu that contains child items.

    Custom Attributes
    -
    - _children : `list[UI_Nav_OBJ]`
        - Collection of child navigation elements contained within the current
            dropdown menu.

    Custom Constants
    -
    None

    Custom Methods
    -
    - __init__(label, children=None, route=None, ...) : `None`
        - Instance Method.
        - Creates a new navigation dropdown menu.
    - _get_data(lvl=0) : `OBJ._DATA`
        - `OBJ` Instance Method.
        - Produces a `dict` of keys and values of the data from the object.

    Custom Properties
    -
    - children : `list[UI_Nav_OBJ]`
        - Collection of child navigation elements.
    - route : `str | None`
        - Route to create a "GET" request that will return a collection of
            `UI_Nav_OBJ` navigation elements. This is used for lazy-loading
            navigation elements to reduce initial loading time.
    - visible : `bool`
        - Flag used to indicate whether or not the navigation element should be
            rendered in the html template.
    '''

    # ===========
    # Constructor
    def __init__(
            self,
            label: str,
            children: Optional[List['UI_Nav_OBJ']] = None,
            route: Optional[str] = None,
            current: bool = False,
            icon: Optional[str] = None,
            count: Optional[int] = None,
            border_top: bool = False,
            border_right: bool = False,
            border_bottom: bool = False,
            border_left: bool = False,
            tooltip: Optional[str] = None,
            confirm: Optional[str] = None
    ) -> None:
        # create base navigation element values
        super().__init__(
            label = label,
            route = route,
            current = current,
            icon = icon,
            count = count,
            border_top = border_top,
            border_right = border_right,
            border_bottom = border_bottom,
            border_left = border_left,
            tooltip = tooltip,
            confirm = confirm
        )

        # creating child elements list
        self._children: list[UI_Nav_OBJ] = [] if children is None else children
        ''' Collection of child navigation elements contained within the
            current dropdown menu. '''

    # ===================
    # Property - Children
    @property
    def children(self) -> List['UI_Nav_OBJ']:
        ''' Collection of child navigation elements. '''
        return self._children

    # ================
    # Property - Route
    @property
    def route(self) -> Optional[str]:
        ''' Route to create a "GET" request that will return a collection of
            `UI_Nav_OBJ` navigation elements. This is used for lazy-loading
            navigation elements to reduce initial loading time. '''
        return self._route

    # ==================
    # Property - Visible
    @property
    def visible(self) -> bool:
        ''' Flag used to indicate whether or not the navigation element should
            be rendered in the html template. '''

        return (
            (self.label != '') # label is not empty
            and ( # dropdown has or will have children
                (self.route is not None) # lazy-loading children
                or (len(self.children) > 0) # already has children
            )
        )

    # =============
    # OBJ: Get Data
    def _get_data(self, lvl: int = 0) -> OBJ._DATA:
        # initialize data
        data = super()._get_data(lvl)

        # short representation
        if lvl == 0:
            data['children'] = len(self.children)

        # long representation
        if lvl == 1:
            data['children'] = self.children

        # debug
        if lvl == 2:
            data['_children'] = self._children
            data['children'] = self.children

        return data


# =============================================================================
# End of File
# =============================================================================
