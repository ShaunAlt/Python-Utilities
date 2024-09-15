# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - User Interface - Tables
-
Contains the objects that can be used to create a dynamic table.

Contents
-
- `UI_Table`
    - Contains the data required to create a table in the user interface.
- `UI_Table_Btns`
    - Contains a collection of flags that can be used to indicate which buttons
        should be displayed in a table or table row.
- `UI_Table_Row`
    - Contains a single row of data for the table.
    
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
    Callable, # callable type (function)
    Dict, # dict type
    List, # list type
    Optional, # optional type
    Tuple, # tuple type
    Union, # union of types
)


# =============================================================================
# User Interface Table
# =============================================================================
class UI_Table(OBJ):
    '''
    User Interface Table
    -
    Contains the data required to create a table in the user interface.

    Custom Attributes
    -
    - _btns_add : `list[tuple[str, str, str]]`
        - Collection of buttons (label, route, tooltip) to use for creating
            new rows in the table.
    - _btns_download : `list[tuple[str, str, str]]`
        - Collection of buttons (label, route, tooltip) to use for downloading
            data from the table.
    - _btns_table : `UI_Table_Btns`
        - Collection of button flags for the overall table.
    - _desc : `str`
        - Description of the table that will be displayed above it.
    - _form : `Any | None`
        - Form that can be used to filter the data in the table. Defaults to
            `None`, meaning that no filter form will be created for the current
            table.
    - _headers : `list[tuple[str, int]]`
        - Collection of column headers (text, col-width) for the table.
    - _rows : `list[UI_Table_Row] | str`
        - If `str`, contains the route to use to lazy-load all of the rows in
            the table. If `list[UI_Table_Row]`, contains the pre-loaded rows
            for the table.
    - _search : `str | None`
        - If `str`, contains the route to use to get the search results for the
            table. If `None`, no search will be performed for the table.
    - _title : `str`
        - Title of the table.

    Custom Constants
    -
    None

    Custom Methods
    -
    - __init__(...) : `None`
        - Instance Method.
        - Creates a new table buttons collection.
    - _get_data(lvl=0) : `OBJ._DATA`
        - `OBJ` Instance Method.
        - Produces a `dict` of keys and values of the data from the object.

    Custom Properties
    -
    - btns_add : `list[tuple[str, str, str]]`
        - Collection of buttons (label, route, tooltip) for adding new rows.
    - btns_download : `list[tuple[str, str, str]]`
        - Collection of buttons (label, route, tooltip) for downloading data.
    - btns_table : `list[str]`
        - Collection of button flags to include in the table.
    - desc : `str`
        - Table description.
    - form : `Any | None`
        - Form used to filter the data in the table.
    - headers : `list[tuple[str, int]]`
        - Collection of column headers (text, col-width) for the table.
    - rows_list : `list[UI_Table_Row]`
        - Collection of pre-loaded rows for the table.
    - rows_str : `str | None`
        - If `str`, contains the route to use to lazy-load all of the rows in
            the table. If `None`, the table will use `rows_list` to populate
            the data.
    - search : `str | None`
        - If `str`, contains the route to use to search the table. If `None`,
            searching will not be performed for this table.
    - title : `str`
        - Table title.
    '''

    # ===========
    # Constructor
    def __init__(
            self,
            title: str,
            desc: str,
            headers: List[Tuple[str, int]],
            rows: Union[str, List['UI_Table_Row']],
            btns_add: Optional[List[Tuple[str, str, str]]] = None,
            btns_download: Optional[List[Tuple[str, str, str]]] = None,
            search: Optional[str] = None,
            form: Optional[Any] = None
    ) -> None:
        # set buttons for adding new rows
        self._btns_add: List[Tuple[str, str, str]] = []
        ''' Collection of buttons (label, route, tooltip) to used for creating
            new rows in the table. '''
        if btns_add is not None: self._btns_add = btns_add

        # set buttons for downloading data
        self._btns_download: List[Tuple[str, str, str]] = []
        ''' Collection of buttons (label, route, tooltip) to use for
            downloading data from the table. '''
        if btns_download is not None: self._btns_download = btns_download

        # set table buttons
        self._btns_table: UI_Table_Btns = UI_Table_Btns() # default to empty
        ''' Collection of button flags for the overall table. '''
        if isinstance(rows, list): # if pre-loaded rows - calculate buttons
            self._btns_table = UI_Table_Btns.from_list([
                row.btns
                for row in rows
            ])

        # set table description
        self._desc: str = desc
        ''' Description of the table that will be displayed above it. '''

        # set table form
        self._form: Optional[Any] = form
        ''' Form that can be used to filter the data in the table. Defaults to
            `None`, meaning that no filter form will be created for the current
            table. '''

        # set table headers
        self._headers: List[Tuple[str, int]] = headers
        ''' Collection of column headers (text, col-width) for the table. '''

        # set table rows
        self._rows: Union[str, list[UI_Table_Row]] = rows
        ''' If `str`, contains the route to use to lazy-load all of the rows in
            the table. If `list[UI_Table_Row]`, contains the pre-loaded rows
            for the table. '''

        # set table search callback
        self._search: Optional[str] = search
        ''' If `str`, contains the route to use to get the search results for
            the table. If `None`, no search will be performed for the
            table. '''
        
        # set table title
        self._title: str = title
        ''' Title of the table. '''
        
    # ============================
    # Property - Buttons - New Row
    @property
    def btns_add(self) -> List[Tuple[str, str, str]]:
        ''' Collection of buttons (label, route, tooltip) for adding new
            rows. '''
        return self._btns_add

    # ==================================
    # Property - Buttons - Download Data
    @property
    def btns_download(self) -> List[Tuple[str, str, str]]:
        ''' Collection of buttons (label, route, tooltip) for downloading
            data. '''
        return self._btns_download
    
    # ==========================
    # Property - Buttons - Table
    @property
    def btns_table(self) -> List[str]:
        ''' Collection of button flags for the overall table. '''
        return [ # creates the order (L-R) the buttons will be displayed
            k
            for k in [
                UI_Table_Btns.KEY_APPROVE,
                UI_Table_Btns.KEY_DECLINE,
                UI_Table_Btns.KEY_COPY,
                UI_Table_Btns.KEY_EDIT,
                UI_Table_Btns.KEY_VIEW,
                UI_Table_Btns.KEY_NEW,
                UI_Table_Btns.KEY_ARCHIVE,
                UI_Table_Btns.KEY_DELETE,
            ]
            if k in self._btns_table.flags.keys()
        ]
    
    # ======================
    # Property - Description
    @property
    def desc(self) -> str:
        ''' Table description. '''
        return self._desc
    
    # ======================
    # Property - Filter Form
    @property
    def form(self) -> Optional[Any]:
        ''' Form used to filter the data in the table. '''
        return self._form
    
    # ==================
    # Property - Headers
    @property
    def headers(self) -> List[Tuple[str, int]]:
        ''' Collection of column headers (text, col-width) for the table. '''
        return self._headers
    
    # =================================
    # Property - Rows - Pre-Loaded List
    @property
    def rows_list(self) -> List['UI_Table_Row']:
        ''' Collection of pre-loaded rows for the table. '''
        if isinstance(self._rows, list): return self._rows
        return []
    
    # ====================================
    # Property - Rows - Lazy-Loading Route
    @property
    def rows_str(self) -> Optional[str]:
        ''' If `str`, contains the route to use to lazy-load all of the rows in
            the table. If `None`, the table will use `rows_list` to populate
            the data. '''
        if isinstance(self._rows, str): return self._rows
        return None
    
    # =======================
    # Property - Search Route
    @property
    def search(self) -> Optional[str]:
        ''' If `str`, contains the route to use to search the table. If `None`,
            searching will not be performed for this table. '''
        return self._search
    
    # =====
    # Title
    @property
    def title(self) -> str:
        ''' Table title. '''
        return self._title
    
    # =============
    # OBJ: Get Data
    def _get_data(self, lvl: int = 0) -> OBJ._DATA:
        # initialize data
        data = super()._get_data(lvl)

        # short representation
        if lvl == 0:
            data['title'] = self.title
            data['headers'] = [h[0] for h in self.headers]
            data['btns'] = self.btns_table

        # long representation
        elif lvl == 1:
            data['btns_add'] = self.btns_add
            data['btns_download'] = self.btns_download
            data['btns_table'] = self.btns_table
            data['desc'] = self.desc
            data['form'] = self.form
            data['headers'] = self.headers
            data['rows_list'] = self.rows_list
            data['rows_str'] = self.rows_str
            data['search'] = self.search
            data['title'] = self.title

        # debug
        elif lvl == 2:
            data['_btns_add'] = self._btns_add
            data['_btns_download'] = self._btns_download
            data['_btns_table'] = self._btns_table
            data['_desc'] = self._desc
            data['_form'] = self._form
            data['_headers'] = self._headers
            data['_rows'] = self._rows
            data['_search'] = self._search
            data['_title'] = self._title
            data['btns_add'] = self.btns_add
            data['btns_download'] = self.btns_download
            data['btns_table'] = self.btns_table
            data['desc'] = self.desc
            data['form'] = self.form
            data['headers'] = self.headers
            data['rows_list'] = self.rows_list
            data['rows_str'] = self.rows_str
            data['search'] = self.search
            data['title'] = self.title

        return data


# =============================================================================
# User Interface Table Buttons
# =============================================================================
class UI_Table_Btns(OBJ):
    '''
    User Interface Table Buttons
    -
    Contains a collection of flags that can be used to indicate which buttons
    should be displayed in a table or table row.

    Custom Attributes
    -
    - _flag_approve : `bool | None`
        - Defaults to `None`, meaning that the button should not be displayed.
            If `True`, the button should be displayed with "Approve" as the
            tooltip. If `False`, the button should not be displayed.
    - _flag_archive : `bool | None`
        - Defaults to `None`, meaning that the button should not be displayed.
            If `True`, the button should be displayed with "Archive" as the
            tooltip. If `False`, the button should be displayed with
            "Unarchive" as the tooltip.
    - _flag_copy : `bool | None`
        - Defaults to `None`, meaning that the button should not be displayed.
            If `True`, the button should be displayed with "Copy" as the
            tooltip. If `False`, the button should not be displayed.
    - _flag_decline : `bool | None`
        - Defaults to `None`, meaning that the button should not be displayed.
            If `True`, the button should be displayed with "Decline" as the
            tooltip. If `False`, the button should not be displayed.
    - _flag_delete : `bool | None`
        - Defaults to `None`, meaning that the button should not be displayed.
            If `True`, the button should be displayed with "Delete" as the
            tooltip. If `False`, the button should not be displayed.
    - _flag_edit : `bool | None`
        - Defaults to `None`, meaning that the button should not be displayed.
            If `True`, the button should be displayed with "Edit" as the
            tooltip. If `False`, the button should not be displayed.
    - _flag_new : `bool | None`
        - Defaults to `None`, meaning that the button should not be displayed.
            If `True`, the button should be displayed with "New" as the
            tooltip. If `False`, the button should not be displayed.
    - _flag_view : `bool | None`
        - Defaults to `None`, meaning that the button should not be displayed.
            If `True`, the button should be displayed with "View" as the
            tooltip. If `False`, the button should not be displayed.

    Custom Constants
    -
    - KEY_APPROVE : `str`
        - Key used in `flags` to indicate the `_flag_approve` flag.
    - KEY_ARCHIVE : `str`
        - Key used in `flags` to indicate the `_flag_archive` flag.
    - KEY_COPY : `str`
        - Key used in `flags` to indicate the `_flag_copy` flag.
    - KEY_DECLINE : `str`
        - Key used in `flags` to indicate the `_flag_decline` flag.
    - KEY_DELETE : `str`
        - Key used in `flags` to indicate the `_flag_delete` flag.
    - KEY_EDIT : `str`
        - Key used in `flags` to indicate the `_flag_edit` flag.
    - KEY_NEW : `str`
        - Key used in `flags` to indicate the `_flag_new` flag.
    - KEY_VIEW : `str`
        - Key used in `flags` to indicate the `_flag_view` flag.

    Custom Methods
    -
    - __init__(...) : `None`
        - Instance Method.
        - Creates a new table buttons collection.
    - _get_data(lvl=0) : `OBJ._DATA`
        - `OBJ` Instance Method.
        - Produces a `dict` of keys and values of the data from the object.
    - from_list(btns) : `UI_Table_Btns`
        - Class Method.
        - Takes a collection of table button flag objects, and returns a new
            table button flag object containing a union of all flags.

    Custom Properties
    -
    - flag_approve : `str | None`
        - Tooltip for the approve button, if being displayed.
    - flag_archive : `str | None`
        - Tooltip for the archive button, if being displayed.
    - flag_copy : `str | None`
        - Tooltip for the copy button, if being displayed.
    - flag_decline : `str | None`
        - Tooltip for the decline button, if being displayed.
    - flag_delete : `str | None`
        - Tooltip for the delete button, if being displayed.
    - flag_edit : `str | None`
        - Tooltip for the edit button, if being displayed.
    - flag_new : `str | None`
        - Tooltip for the new button, if being displayed.
    - flag_view : `str | None`
        - Tooltip for the view button, if being displayed.
    - flags : `dict[str, str]`
        - Collection of buttons being shown, and the corresponding tooltip.
    '''

    # =========
    # Constants
    KEY_APPROVE = 'approve'
    ''' Key used in `flags` to indicate the `_flag_approve` flag. '''
    KEY_ARCHIVE = 'archive'
    ''' Key used in `flags` to indicate the `_flag_archive` flag. '''
    KEY_COPY = 'copy'
    ''' Key used in `flags` to indicate the `_flag_copy` flag. '''
    KEY_DECLINE = 'decline'
    ''' Key used in `flags` to indicate the `_flag_decline` flag. '''
    KEY_DELETE = 'delete'
    ''' Key used in `flags` to indicate the `_flag_delete` flag. '''
    KEY_EDIT = 'edit'
    ''' Key used in `flags` to indicate the `_flag_edit` flag. '''
    KEY_NEW = 'new'
    ''' Key used in `flags` to indicate the `_flag_new` flag. '''
    KEY_VIEW = 'view'
    ''' Key used in `flags` to indicate the `_flag_view` flag. '''

    # ===========
    # Constructor
    def __init__(
            self,
            flag_approve: Optional[bool] = None,
            flag_archive: Optional[bool] = None,
            flag_copy: Optional[bool] = None,
            flag_decline: Optional[bool] = None,
            flag_delete: Optional[bool] = None,
            flag_edit: Optional[bool] = None,
            flag_new: Optional[bool] = None,
            flag_view: Optional[bool] = None
    ) -> None:
        # set approve flag
        self._flag_approve: Optional[bool] = flag_approve
        ''' Defaults to `None`, meaning that the button should not be
            displayed. If `True`, the button should be displayed with "Approve"
            as the tooltip. If `False`, the button should not be displayed. '''
        
        # set archive flag
        self._flag_archive: Optional[bool] = flag_archive
        ''' Defaults to `None`, meaning that the button should not be
            displayed. If `True`, the button should be displayed with "Archive"
            as the tooltip. If `False`, the button should be displayed with
            "Unarchive" as the tooltip. '''
        
        # set copy flag
        self._flag_copy: Optional[bool] = flag_copy
        ''' Defaults to `None`, meaning that the button should not be
            displayed. If `True`, the button should be displayed with "Copy"
            as the tooltip. If `False`, the button should not be displayed. '''

        # set decline flag
        self._flag_decline: Optional[bool] = flag_decline
        ''' Defaults to `None`, meaning that the button should not be
            displayed. If `True`, the button should be displayed with "Decline"
            as the tooltip. If `False`, the button should not be displayed. '''
        
        # set delete flag
        self._flag_delete: Optional[bool] = flag_delete
        ''' Defaults to `None`, meaning that the button should not be
            displayed. If `True`, the button should be displayed with "Delete"
            as the tooltip. If `False`, the button should not be displayed. '''
        
        # set edit flag
        self._flag_edit: Optional[bool] = flag_edit
        ''' Defaults to `None`, meaning that the button should not be
            displayed. If `True`, the button should be displayed with "Edit"
            as the tooltip. If `False`, the button should not be displayed. '''
        
        # set new flag
        self._flag_new: Optional[bool] = flag_new
        ''' Defaults to `None`, meaning that the button should not be
            displayed. If `True`, the button should be displayed with "New"
            as the tooltip. If `False`, the button should not be displayed. '''
        
        # set view flag
        self._flag_view: Optional[bool] = flag_view
        ''' Defaults to `None`, meaning that the button should not be
            displayed. If `True`, the button should be displayed with "View"
            as the tooltip. If `False`, the button should not be displayed. '''
        
    # =========================
    # Property - Flag - Approve
    @property
    def flag_approve(self) -> Optional[str]:
        ''' Tooltip for the approve button, if being displayed. '''
        return 'Approve' if self._flag_approve else None

    # =====================================
    # Property - Flag - Archive / Unarchive
    @property
    def flag_archive(self) -> Optional[str]:
        ''' Tooltip for the archive button, if being displayed. '''
        if self._flag_archive is None: return None
        return 'Archive' if self._flag_archive else 'Unarchive'
    
    # ======================
    # Property - Flag - Copy
    @property
    def flag_copy(self) -> Optional[str]:
        ''' Tooltip for the copy button, if being displayed. '''
        return 'Copy' if self._flag_copy else None

    # =========================
    # Property - Flag - Decline
    @property
    def flag_decline(self) -> Optional[str]:
        ''' Tooltip for the decline button, if being displayed. '''
        return 'Decline' if self._flag_decline else None

    # ========================
    # Property - Flag - Delete
    @property
    def flag_delete(self) -> Optional[str]:
        ''' Tooltip for the delete button, if being displayed. '''
        return 'Delete' if self._flag_delete else None

    # ======================
    # Property - Flag - Edit
    @property
    def flag_edit(self) -> Optional[str]:
        ''' Tooltip for the edit button, if being displayed. '''
        return 'Edit' if self._flag_edit else None
    
    # =====================
    # Property - Flag - New
    @property
    def flag_new(self) -> Optional[str]:
        ''' Tooltip for the new button, if being displayed. '''
        return 'New' if self._flag_new else None

    # ======================
    # Property - Flag - View
    @property
    def flag_view(self) -> Optional[str]:
        ''' Tooltip for the view button, if being displayed. '''
        return 'View' if self._flag_view else None
    
    # ===========================
    # Property - Flags Collection
    @property
    def flags(self) -> Dict[str, str]:
        ''' Collection of buttons being shown, and the corresponding
            tooltip. '''
        
        # initialize flags collection
        flags: Dict[str, str] = {}

        # add flags
        if self.flag_approve is not None: # approve / decline flag
            flags[UI_Table_Btns.KEY_APPROVE] = self.flag_approve
        if self.flag_archive is not None: # archive / unarchive flag
            flags[UI_Table_Btns.KEY_ARCHIVE] = self.flag_archive
        if self.flag_copy is not None: # copy flag
            flags[UI_Table_Btns.KEY_COPY] = self.flag_copy
        if self.flag_decline is not None: # decline flag
            flags[UI_Table_Btns.KEY_DECLINE] = self.flag_decline
        if self.flag_delete is not None: # delete flag
            flags[UI_Table_Btns.KEY_DELETE] = self.flag_delete
        if self.flag_edit is not None: # edit flag
            flags[UI_Table_Btns.KEY_EDIT] = self.flag_edit
        if self.flag_new is not None: # new flag
            flags[UI_Table_Btns.KEY_NEW] = self.flag_new
        if self.flag_view is not None: # view flag
            flags[UI_Table_Btns.KEY_VIEW] = self.flag_view

        return flags
    
    # =============
    # OBJ: Get Data
    def _get_data(self, lvl: int = 0) -> OBJ._DATA:
        # initialize data
        data = super()._get_data(lvl)

        # short representation
        if lvl == 0:
            data['flags'] = [k for k in self.flags.keys()]

        # long representation
        elif lvl == 1:
            data['flag_approve'] = self.flag_approve
            data['flag_archive'] = self.flag_archive
            data['flag_copy'] = self.flag_copy
            data['flag_decline'] = self.flag_decline
            data['flag_delete'] = self.flag_delete
            data['flag_edit'] = self.flag_edit
            data['flag_new'] = self.flag_new
            data['flag_view'] = self.flag_view
            data['flags'] = self.flags

        # debug
        elif lvl == 2:
            data['_flag_approve'] = self._flag_approve
            data['_flag_archive'] = self._flag_archive
            data['_flag_copy'] = self._flag_copy
            data['_flag_decline'] = self._flag_decline
            data['_flag_delete'] = self._flag_delete
            data['_flag_edit'] = self._flag_edit
            data['_flag_new'] = self._flag_new
            data['_flag_view'] = self._flag_view
            data['flag_approve'] = self.flag_approve
            data['flag_archive'] = self.flag_archive
            data['flag_copy'] = self.flag_copy
            data['flag_decline'] = self.flag_decline
            data['flag_delete'] = self.flag_delete
            data['flag_edit'] = self.flag_edit
            data['flag_new'] = self.flag_new
            data['flag_view'] = self.flag_view
            data['flags'] = self.flags
            data['KEY_APPROVE'] = self.KEY_APPROVE
            data['KEY_ARCHIVE'] = self.KEY_ARCHIVE
            data['KEY_COPY'] = self.KEY_COPY
            data['KEY_DECLINE'] = self.KEY_DECLINE
            data['KEY_DELETE'] = self.KEY_DELETE
            data['KEY_EDIT'] = self.KEY_EDIT
            data['KEY_NEW'] = self.KEY_NEW
            data['KEY_VIEW'] = self.KEY_VIEW

        return data

    # ========================
    # Create Buttons from List
    @classmethod
    def from_list(cls, btns: List['UI_Table_Btns']) -> 'UI_Table_Btns':
        '''
        Create Buttons from List
        -
        Takes a collection of table button flag objects, and returns a new
        table button flag object containing a union of all flags.

        Parameters
        -
        - btns : `list[UI_Table_Btns]`
            - A collection of table button flag objects to create the union
                from.

        Returns
        -
        - `UI_Table_Btns`
            - New table button flag object containing a union of all flags.
        '''

        # create collection of all flags
        flags: List[str] = list(set([
            flag_key
            for btn in btns
            for flag_key in btn.flags.keys()
        ]))

        # key bool to flag value map
        bool_to_flag: Dict[bool, Optional[bool]] = {
            True: True, # default value - always displays
            False: None, # if flag not present - None to prevent display
        }

        # create new button from union
        return cls(
            flag_approve = bool_to_flag[UI_Table_Btns.KEY_APPROVE in flags],
            flag_archive = bool_to_flag[UI_Table_Btns.KEY_ARCHIVE in flags],
            flag_copy = bool_to_flag[UI_Table_Btns.KEY_COPY in flags],
            flag_decline = bool_to_flag[UI_Table_Btns.KEY_DECLINE in flags],
            flag_delete = bool_to_flag[UI_Table_Btns.KEY_DELETE in flags],
            flag_edit = bool_to_flag[UI_Table_Btns.KEY_EDIT in flags],
            flag_new = bool_to_flag[UI_Table_Btns.KEY_NEW in flags],
            flag_view = bool_to_flag[UI_Table_Btns.KEY_VIEW in flags]
        )


# =============================================================================
# User Interface Table Row
# =============================================================================
class UI_Table_Row(OBJ):
    '''
    User Interface Table Row.
    -
    Contains a single row of data for the table.

    Custom Attributes
    -
    - _btns : `UI_Table_Btns`
        - Collection of button flags for the current row.
    - _cells : `list[tuple[str, int]]`
        - Collection of data cells (text, col-width) for the current row.
    - _children : `list[UI_Table_Row] | str | None`
        - If `None`, the current row has no children. If `str`, this contains
            the route to use to lazy-load the children of the current row.
            Otherwise, contains the children of the current row.
    - _depth : `int`
        - Number of parent rows the current row has.
    - _id : `str`
        - ID of the object being displayed in the current row.
    - _route_func : `(str) -> str`
        - Function which will take the type of the button that was clicked, and
            will return an appropriate route.
        - Example: `lambda x: flask.url_for('my_route', access_type=x)`

    Custom Constants
    -
    - MAX_DEPTH : `int`
        - Maximum depth that rows will be displayed at. They will still store
            their actual depth, but when rendered their depth will be capped at
            this value.

    Custom Methods
    -
    - __init__(id, cells, btns, route_func, children=None, depth=0) : `None`
        - Instance Method.
        - Creates a new table row.
    - _get_data(lvl=0) : `OBJ._DATA`
        - `OBJ` Instance Method.
        - Produces a `dict` of keys and values of the data from the object.

    Custom Properties
    -
    - btn_approve : `tuple[str, str] | None`
        - Contains the (route, tooltip) of the approve button, if displayed.
    - btn_archive : `tuple[str, str] | None`
        - Contains the (route, tooltip) of the archive button, if displayed.
    - btn_copy : `tuple[str, str] | None`
        - Contains the (route, tooltip) of the copy button, if displayed.
    - btn_decline : `tuple[str, str] | None`
        - Contains the (route, tooltip) of the decline button, if displayed.
    - btn_delete : `tuple[str, str] | None`
        - Contains the (route, tooltip) of the delete button, if displayed.
    - btn_edit : `tuple[str, str] | None`
        - Contains the (route, tooltip) of the edit button, if displayed.
    - btn_new : `tuple[str, str] | None`
        - Contains the (route, tooltip) of the new button, if displayed.
    - btn_view : `tuple[str, str] | None`
        - Contains the (route, tooltip) of the view button, if displayed.
    - btns : `UI_Table_Btns`
        - Collection of button flags for the current row.
    - btns_dict : `dict[str, tuple[str, str] | None]`
        - Dictionary of button keys, and the corresponding button value.
    - cells : `list[tuple[str, int]]`
        - Collcetion of data cells (text, col-width) for the current row.
    - children_rows : `list[UI_Table_Row]`
        - Contains a collection of pre-loaded child rows for the current row.
    - children_str : `str | None`
        - If `str`, contains the route used for lazy loading children of the
            current row. `None` means lazy loading is not happening for this
            row.
    - depth : `int`
        - Number of parent rows the current row has. Capped by `MAX_DEPTH`.
    - has_children : `bool`
        - Whether or not the current row has children.
    - id : `str`
        - ID of the object being displayed in the current row.
    '''

    # =========
    # Constants
    MAX_DEPTH = 5
    ''' Maximum depth that rows will be displayed at. They will still store
        their actual depth, but when rendered their depth will be capped at
        this value. '''

    # ===========
    # Constructor
    def __init__(
            self,
            id: str,
            cells: List[Tuple[str, int]],
            btns: 'UI_Table_Btns',
            route_func: Callable[[str], str],
            children: Union[List['UI_Table_Row'], str, None] = None,
            depth: int = 0
    ) -> None:
        # set row buttons
        self._btns: UI_Table_Btns = btns
        ''' Collection of button flags for the current row. '''

        # set row cells
        self._cells: List[Tuple[str, int]] = cells
        ''' Collection of data cells (text, col-width) for the current row. '''

        # set row children
        self._children: Union[List['UI_Table_Row'], str, None] = children
        ''' If `None`, the current row has no children. If `str`, this contains
            the route to use to lazy-load the children of the current row.
            Otherwise, contains the children of the current row. '''

        # set row depth
        self._depth: int = max(depth, 0) # make sure depth is not negative
        ''' Number of parent rows the current row has. '''

        # set row id
        self._id: str = id
        ''' ID of the object being displayed in the current row. '''

        # set route generator function
        self._route_func: Callable[[str], str] = route_func
        ''' Function which will take the type of the button that was clicked,
            and will return an appropriate route. '''

        # children - convert to `None` if other value was invalid
        if self._children == '': self._children = None # empty string invalid
        elif self._children == []: self._children = None # empty list invalid

    # ===========================
    # Property - Button - Approve
    @property
    def btn_approve(self) -> Optional[Tuple[str, str]]:
        ''' Contains the (route, tooltip) of the approve button, if
            displayed. '''

        # if button not being displayed - return None
        if self._btns.flag_approve is None: return None

        # return route + tooltip
        return (
            self._route_func(UI_Table_Btns.KEY_APPROVE), # generate route
            self._btns.flag_approve # get tooltip
        )
    
    # ===========================
    # Property - Button - Archive
    @property
    def btn_archive(self) -> Optional[Tuple[str, str]]:
        ''' Contains the (route, tooltip) of the archive button, if
            displayed. '''

        # if button not being displayed - return None
        if self._btns.flag_archive is None: return None

        # return route + tooltip
        return (
            self._route_func(UI_Table_Btns.KEY_ARCHIVE), # generate route
            self._btns.flag_archive # get tooltip
        )

    # ========================
    # Property - Button - Copy
    @property
    def btn_copy(self) -> Optional[Tuple[str, str]]:
        ''' Contains the (route, tooltip) of the copy button, if displayed. '''

        # if button not being displayed - return None
        if self._btns.flag_copy is None: return None

        # return route + tooltip
        return (
            self._route_func(UI_Table_Btns.KEY_COPY), # generate route
            self._btns.flag_copy # get tooltip
        )

    # ===========================
    # Property - Button - Decline
    @property
    def btn_decline(self) -> Optional[Tuple[str, str]]:
        ''' Contains the (route, tooltip) of the decline button, if
            displayed. '''

        # if button not being displayed - return None
        if self._btns.flag_decline is None: return None

        # return route + tooltip
        return (
            self._route_func(UI_Table_Btns.KEY_DECLINE), # generate route
            self._btns.flag_decline # get tooltip
        )

    # ==========================
    # Property - Button - Delete
    @property
    def btn_delete(self) -> Optional[Tuple[str, str]]:
        ''' Contains the (route, tooltip) of the delete button, if
            displayed. '''

        # if button not being displayed - return None
        if self._btns.flag_delete is None: return None

        # return route + tooltip
        return (
            self._route_func(UI_Table_Btns.KEY_DELETE), # generate route
            self._btns.flag_delete # get tooltip
        )

    # ========================
    # Property - Button - Edit
    @property
    def btn_edit(self) -> Optional[Tuple[str, str]]:
        ''' Contains the (route, tooltip) of the edit button, if displayed. '''

        # if button not being displayed - return None
        if self._btns.flag_edit is None: return None

        # return route + tooltip
        return (
            self._route_func(UI_Table_Btns.KEY_EDIT), # generate route
            self._btns.flag_edit # get tooltip
        )

    # =======================
    # Property - Button - New
    @property
    def btn_new(self) -> Optional[Tuple[str, str]]:
        ''' Contains the (route, tooltip) of the new button, if displayed. '''

        # if button not being displayed - return None
        if self._btns.flag_new is None: return None

        # return route + tooltip
        return (
            self._route_func(UI_Table_Btns.KEY_NEW), # generate route
            self._btns.flag_new # get tooltip
        )

    # ========================
    # Property - Button - View
    @property
    def btn_view(self) -> Optional[Tuple[str, str]]:
        ''' Contains the (route, tooltip) of the view button, if displayed. '''

        # if button not being displayed - return None
        if self._btns.flag_view is None: return None

        # return route + tooltip
        return (
            self._route_func(UI_Table_Btns.KEY_VIEW), # generate route
            self._btns.flag_view # get tooltip
        )

    # =======================
    # Property - Button Flags
    @property
    def btns(self) -> 'UI_Table_Btns':
        ''' Collection of button flags for the current row. '''
        return self._btns
    
    # ===============================
    # Property - Buttons Key / Values
    @property
    def btns_dict(self) -> Dict[str, Optional[Tuple[str, str]]]:
        ''' Dictionary of button keys, and the corresponding button value. '''
        return {
            UI_Table_Btns.KEY_APPROVE: self.btn_approve,
            UI_Table_Btns.KEY_ARCHIVE: self.btn_archive,
            UI_Table_Btns.KEY_COPY: self.btn_copy,
            UI_Table_Btns.KEY_DECLINE: self.btn_decline,
            UI_Table_Btns.KEY_DELETE: self.btn_delete,
            UI_Table_Btns.KEY_EDIT: self.btn_edit,
            UI_Table_Btns.KEY_NEW: self.btn_new,
            UI_Table_Btns.KEY_VIEW: self.btn_view,
        }
    
    # =====================
    # Property - Data Cells
    @property
    def cells(self) -> List[Tuple[str, int]]:
        ''' Collection of data cells (text, col-width) for the current row. '''
        return self._cells
    
    # =====================================
    # Property - Children Rows - Pre-Loaded
    @property
    def children_rows(self) -> List['UI_Table_Row']:
        ''' Contains a collection of pre-loaded child rows for the current row. '''
        return self._children if isinstance(self._children, list) else []

    # ====================================
    # Property - Children Rows - Lazy Load
    @property
    def children_str(self) -> Optional[str]:
        ''' If `str`, contains the route used for lazy loading children of the
            current row. `None` means lazy loading is not happening for this
            row. '''
        return self._children if isinstance(self._children, str) else None

    # ================
    # Property - Depth
    @property
    def depth(self) -> int:
        ''' Number of parent rows the current row has. Capped by
            `MAX_DEPTH`. '''
        return min(self._depth, UI_Table_Row.MAX_DEPTH)

    # =======================
    # Property - Has Children
    @property
    def has_children(self) -> bool:
        ''' Whether or not the current row has children. '''
        return self._children is not None
    
    # ====================
    # Property - Unique ID
    @property
    def id(self) -> str:
        ''' ID of the object being displayed in the current row. '''
        return self._id
    
    # =============
    # OBJ: Get Data
    def _get_data(self, lvl: int = 0) -> OBJ._DATA:
        # initialize data
        data = super()._get_data(lvl)

        # short representation
        if lvl == 0:
            data['id'] = self.id
            data['cells'] = len(self.cells)
            data['btns'] = [k for k in self.btns.flags.keys()]
            data['children'] = type(self._children)

        # long representation
        elif lvl == 1:
            data['btn_approve'] = self.btn_approve
            data['btn_archive'] = self.btn_archive
            data['btn_copy'] = self.btn_copy
            data['btn_decline'] = self.btn_decline
            data['btn_delete'] = self.btn_delete
            data['btn_edit'] = self.btn_edit
            data['btn_new'] = self.btn_new
            data['btn_view'] = self.btn_view
            data['btns'] = self.btns
            data['btns_dict'] = self.btns_dict
            data['cells'] = self.cells
            data['children_rows'] = self.children_rows
            data['children_str'] = self.children_str
            data['depth'] = self.depth
            data['has_children'] = self.has_children
            data['id'] = self.id

        # debug
        elif lvl == 2:
            data['_btns'] = self._btns
            data['_cells'] = self._cells
            data['_children'] = self._children
            data['_depth'] = self._depth
            data['_id'] = self._id
            data['_route_func'] = self._route_func
            data['btn_approve'] = self.btn_approve
            data['btn_archive'] = self.btn_archive
            data['btn_copy'] = self.btn_copy
            data['btn_decline'] = self.btn_decline
            data['btn_delete'] = self.btn_delete
            data['btn_edit'] = self.btn_edit
            data['btn_new'] = self.btn_new
            data['btn_view'] = self.btn_view
            data['btns'] = self.btns
            data['btns_dict'] = self.btns_dict
            data['cells'] = self.cells
            data['children_rows'] = self.children_rows
            data['children_str'] = self.children_str
            data['depth'] = self.depth
            data['has_children'] = self.has_children
            data['id'] = self.id
            data['MAX_DEPTH'] = self.MAX_DEPTH

        return data


# =============================================================================
# End of File
# =============================================================================
