# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - User Interface - Page
-
Contains the objects that can be used to create a dynamic web-page.

Contents
-
- `UI_Page`
    - Contains the data required to create a web-page in the user interface.
    
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
- `.nav`
    - Used for creating a navigation menu.
    - `ui_utils.nav`.
- `.table`
    - Used for creating page tables.
    - `ui_utils.table`.
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

# used for base object definition
from ..generic_utils import OBJ

# used for creating a navigation menu
from .nav import UI_Nav_OBJ

# used for creating page tables
from .table import UI_Table

# used for string type hints
from __future__ import annotations

# used for getting date/time
from datetime import datetime

# used for type hinting
from typing import (
    Any, # any type
    Dict, # dict type
    List, # list type
    Optional, # optional type
)


# =============================================================================
# User Interface Page Definition
# =============================================================================
class UI_Page(OBJ):
    '''
    User Interface Page
    -
    Contains the data required to create a web-page in the user interface.

    Custom Attributes
    -
    - _code : `str | None`
        - Unique code used to identify the current page that has been selected
            in the navigation menu.
    - _dt : `datetime`
        - Date/Time the page was created at.
    - _forms : `dict[str, Any]`
        - Collection of form names + data implemented in the page.
    - _log : `logging.Logger`
        - Logger used to log 
    - _nav : `list[UI_Nav_OBJ]`
        - Navigation menu objects.
    - _tables : `list[UI_Table_OBJ]`
        - Collection of tables implemented in the page.
    - _title : `str`
        - Page and Tab Title.
    - _title_prefix : `str`
        - Prefix added to the start of the title when getting the tab title.

    Custom Constants
    -
    None

    Custom Methods
    -
    - __init__(title, ...) : `None`
        - Instance Method.
        - Creates a new navigation element.
    - _get_data(lvl=0) : `OBJ._DATA`
        - `OBJ` Instance Method.
        - Produces a `dict` of keys and values of the data from the object.
    - create_nav(_time=-1) : `None`
        - Instance Method.
        - Creates all of the navigation menu items for the current page.
    - render(html, _time=-1, **kwargs) : `str`
        - Instance Method.
        - Renders the page using the provided HTML template.

    Custom Properties
    -
    - code : `str | None`
        - Unique code of the current page.
    - dt : `datetime`
        - Date/Time the page was created at.
    - forms : `dict[str, Any]`
        - Collection of form names + data implemented in the page.
    - nav : `list[UI_Nav_OBJ]`
        - Navigation menu objects.
    - tables : `list[UI_Table_OBJ]`
        - Collection of tables implemented in the page.
    - title_main : `str`
        - Main page title.
    - title_tab : `str`
        - Title for the page tab.
    '''

    # ===========
    # Constructor
    def __init__(
            self,
            title: str,
            code: Optional[str] = None,
            forms: Optional[Dict[str, Any]] = None,
            tables: Optional[List[UI_Table]] = None,
            title_prefix: str = 'APP NAME'
    ) -> None:
        # set page code
        self._code: Optional[str] = code
        ''' Unique code used to identify the current page that has been
            selected in the navigation menu. '''

        # set page creation date/time
        self._dt: datetime = datetime.now()
        ''' Date/Time the page was created at. '''

        # set page forms
        self._forms: Dict[str, Any] = forms or {}
        ''' Collection of form names + data implemented in the page. '''

        # set navigation menu
        self._nav: List[UI_Nav_OBJ] = []
        ''' Navigation menu objects. '''

        # set page tables
        self._tables: List[UI_Table] = tables or []
        ''' Collection of tables implemented in the page. '''

        # set page title
        self._title: str = title
        ''' Page and Tab Title. '''

        # set page title prefix
        self._title_prefix: str = title_prefix
        ''' Prefix added to the start of the title when getting the tab
            title. '''

    # ======================
    # Property - Unique Code
    @property
    def code(self) -> Optional[str]:
        ''' Unique code of the current page. '''
        return self._code
    
    # =============================
    # Property - Creation Date/Time
    @property
    def dt(self) -> datetime:
        ''' Date/Time the page was created at. '''
        return self._dt
    
    # ================
    # Property - Forms
    @property
    def forms(self) -> Dict[str, Any]:
        ''' Collection of form names + data implemented in the page. '''
        return self._forms
    
    # ================================
    # Property - Navigation Menu Items
    @property
    def nav(self) -> List[UI_Nav_OBJ]:
        ''' Navigation menu objects. '''
        return self._nav
    
    # =================
    # Property - Tables
    @property
    def tables(self) -> List[UI_Table]:
        ''' Collection of tables implemented in the page. '''
        return self._tables
    
    # ==========================
    # Property - Main Page Title
    @property
    def title_main(self) -> str:
        ''' Main page title. '''
        return self._title
    
    # =========================
    # Property - Page Tab Title
    @property
    def title_tab(self) -> str:
        ''' Title for the page tab. '''
        return f'{self._title_prefix}{self._title}'
    
    # =============
    # OBJ: Get Data
    def _get_data(self, lvl: int = 0) -> OBJ._DATA:
        # initialize data
        data = super()._get_data(lvl)

        # short representation
        if lvl == 0:
            data['code'] = self.code
            data['title'] = self.title_main

        # long representation
        elif lvl == 1:
            data['code'] = self.code
            data['dt'] = self.dt
            data['forms'] = self.forms
            data['nav'] = self.nav
            data['tables'] = self.tables
            data['title_main'] = self.title_main
            data['title_tab'] = self.title_tab

        # debug
        elif lvl == 2:
            data['_code'] = self._code
            data['_dt'] = self._dt
            data['_forms'] = self._forms
            data['_nav'] = self._nav
            data['_tables'] = self._tables
            data['_title'] = self._title
            data['_title_prefix'] = self._title_prefix
            data['code'] = self.code
            data['dt'] = self.dt
            data['forms'] = self.forms
            data['nav'] = self.nav
            data['tables'] = self.tables
            data['title_main'] = self.title_main
            data['title_tab'] = self.title_tab

        return data
    
    # ======================
    # Create Navigation Menu
    def create_nav(self, _time: int = -1) -> None:
        '''
        Create Navigation Menu
        -
        Creates all of the navigation menu items for the current page.

        Parameters
        -
        - _time : `int`
            - `TIMER` verbosity indentation level.

        Returns
        -
        None
        '''

        raise NotImplementedError(
            f'UI_Page().create_nav(_time={_time}) not defined in ' \
            + f'{self.__class__.__name__}'
        )
    
    # ===========
    # Render Page
    def render(
            self,
            html: str,
            _time: int = -1,
            **kwargs: Any
    ) -> str:
        '''
        Render Page
        -
        Renders the page using the provided HTML template.

        Parameters
        -
        - html : `str`
            - Filename + path of to the HTML template document.
        - _time : `int`
            - `TIMER` verbosity indentation level.
        - **kwargs : `Any`
            - Additional keyword arguments to use when rendering the HTML
                template.

        Returns
        -
        - `str`
            - String representation of the HTML template.
        '''

        raise NotImplementedError(
            f'UI_Page().render({html}, _time={_time}, kwargs={kwargs}) not ' \
            + f'defined in {self.__class__.__name__}'
        )


# =============================================================================
# End of File
# =============================================================================
