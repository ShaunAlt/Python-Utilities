# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - XLSX - Models
-
Contains the definitions of the model objects used for creating .xlsx files.

Contents
-
- `XLSX_Book`
    - Contains the data required to create an individual .xlsx workbook file.
- `XLSX_Header`
    - Contains the data for a single column header in an .xlsx sheet.
- `XLSX_Sheet`
    - Contains the data required to create an individual sheet in an .xlsx
        file.

Dependencies
-
- `io`
    - Used for storing raw file content.
    - Builtin.
- `typing`
    - Used for type hinting.
    - Builtin.
- `xlsxwriter`
    - Used for creating the xlsx document.
    - `xlsxwriter==3.2.0`

Internal Dependencies
-
- `generic_utils`
    - Used for base object definition.
    - `generic_utils`.
- `.errors`
    - Used for custom exceptions.
    - `xlsx_utils.errors`.
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

# used for base object
from ..generic_utils import OBJ

# used for custom exceptions
from .errors import (
    PreExistingColumnID,
)

# used for storing raw file content
from io import BytesIO

# used for type hinting
from typing import (
    Any, # any type
    Dict, # dict type
    List, # list type
    Optional, # optional type
    Tuple, # tuple type
)


# =============================================================================
# XLSX Model Definitions
# =============================================================================

# ====
# Book
class XLSX_Book(OBJ):
    '''
    XLSX Workbook
    -
    Contains the data required to create an individual .xlsx workbook file.

    Custom Attributes
    -
    - _sheets : `list[XLSX_Sheet]`
        - Collection of sheets that the .xlsx workbook will contain.

    Custom Constants
    -
    None

    Custom Methods
    -
    - __init__(sheets=None) : `None`
        - Instance Method.
        - Initializes the workbook with the specified filename and sheets.
    - _get_data(lvl=0) : `OBJ._DATA`
        - `OBJ` Instance Method.
        - Produces a `dict` of keys and values of the data from the object.
    - add_sheet(new_sheet) : `None`
        - Instance Method.
        - Adds a new sheet to the collection of sheets in the workbook.
    - create() : `BytesIO`
        - Instance Method.
        - Converts all of the workbook objects and data into a single in-memory
            .xlsx file which is stored as a `BytesIO` object.

    Custom Properties
    -
    - sheets : `list[XLSX_Sheet]`
        - Collection of sheets that the .xlsx workbook will contain.
    '''

    # ===========
    # Constructor
    def __init__(self, sheets: Optional[List['XLSX_Sheet']] = None) -> None:
        # initialize the sheets collection
        self._sheets: list[XLSX_Sheet] = [] if sheets is None else sheets
        ''' Collection of sheets that the .xlsx workbook will contain. '''

    # ==========================
    # Property - Workbook Sheets
    @property
    def sheets(self) -> list['XLSX_Sheet']:
        ''' Collection of sheets that the .xlsx workbook will contain. '''
        return self._sheets

    # =============
    # OBJ: Get Data
    def _get_data(self, lvl: int = 0) -> OBJ._DATA:
        # initialize data
        data = super()._get_data(lvl)

        # short representation
        if lvl == 0:
            data = {
                '# sheets': len(self.sheets),
            }

        # long representation / debug
        elif lvl in [1, 2]:
            data = {
                'sheets': self.sheets,
            }

        return data

    # =============
    # Add New Sheet
    def add_sheet(self, new_sheet: 'XLSX_Sheet') -> None:
        '''
        Add New Sheet
        -
        Add a new sheet to the collection of sheets in the workbook.

        Properties
        -
        - new_sheet : `XLSX_Sheet`
            - New sheet to add to the workbook.

        Returns
        -
        None
        '''

        self._sheets.append(new_sheet)

    # ====================
    # Create Workbook File
    def create(self) -> BytesIO:
        '''
        Create Workbook File
        -
        Converts all of the workbook objects and data into a single in-memory
        .xlsx file which is stored as a `BytesIO` object.

        Parameters
        -
        None

        Returns
        -
        - `BytesIO`
            - In-memory representation of the .xlsx workbook file.
        '''

        # 3rd party library imports
        from xlsxwriter import Workbook # xlsx workbook
        from xlsxwriter.format import Format # cell format
        from xlsxwriter.worksheet import Worksheet # xlsx sheet

        # initialize variables
        b: Workbook # xlsx workbook object
        col_data: str # string data to write in a particular cell
        col_header: XLSX_Header # header for a particular column
        col_id: str # unique identifier for the column
        col_num: int # column number of a particular cell (0 indexed)
        f: BytesIO # in-memory file containing the final workbook data
        format_normal: Format # default cell format
        row: XLSX_Sheet._ROW # single row of worksheet data
        row_num: int # enumeration index for the row number in a sheet of data
        s: Worksheet # xlsx sheet
        sheet: XLSX_Sheet # individual sheet data object

        # create in-memory file for new xlsx document
        f = BytesIO()
        b = Workbook(f, {'in_memory': True})

        # create default cell format
        format_normal = b.add_format()
        format_normal.set_text_wrap()

        # create all of the sheets
        for sheet in self.sheets:
            # create new sheet
            s = b.add_worksheet(s.name)

            # create sheet headers
            for col_num, col_header in sheet.headers.values():
                s.write(0, col_num, col_header.label)
                s.set_column(
                    first_col = col_num,
                    last_col = col_num,
                    width = col_header.width,
                    cell_format = format_normal
                )

            # create sheet rows data
            for row_num, row in enumerate(sheet.data):
                for col_id, col_data in row.items():
                    # only write data if column exists
                    if col_id not in sheet.headers: continue

                    # write data in cell
                    s.write(row_num + 1, sheet.headers[col_id][0], col_data)

        # close workbook to enable reading of the data
        b.close()

        # return in-memory file
        return f

# ======
# Header
class XLSX_Header(OBJ):
    '''
    XLSX Header
    -
    Contains the data for a single column header in an .xlsx sheet.

    Custom Attributes
    -
    - _label : `str`
        - Label text for the column.
    - _width : `int`
        - Width of the column.

    Custom Constants
    -
    None

    Custom Methods
    -
    - __eq__(other) : `bool`
        - Instance Method.
        - Determines if the current header is equal to the other header.
    - __init__(label, width) : `None`
        - Instance Method.
        - Initializes the xlsx header with the given label and column width.
    - _get_data(lvl=0) : `OBJ._DATA`
        - `OBJ` Instance Method.
        - Produces a `dict` of keys and values of the data from the object.

    Custom Properties
    -
    - label : `str`
        - Label text for the column.
    - width : `int`
        - Width of the column.
    '''

    # ==============
    # Equality Check
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, XLSX_Header): return False
        return (
            (self.label == other.label)
            and (self.width == other.width)
        )

    # ===========
    # Constructor
    def __init__(self, label: str, width: int) -> None:
        # set header label
        self._label: str = label
        ''' Label text for the column. '''

        # set header width
        self._width: int = width
        ''' Width of the column. '''

    # =======================
    # Property - Header Label
    @property
    def label(self) -> str:
        ''' Label text for the column. '''
        return self._label

    # =======================
    # Property - Column Width
    @property
    def width(self) -> int:
        ''' Width of the column. '''
        return self._width

    # =============
    # OBJ: Get Data
    def _get_data(self, lvl: int = 0) -> OBJ._DATA:
        # initialize data
        data = super()._get_data(lvl)

        # short representation
        if lvl == 0:
            data = {
                'label': self._label,
                'width': self._width,
            }

        # long representation
        elif lvl in [1, 2]:
            data = {
                'label': self._label,
                'width': self._width,
            }

        return data

# =====
# Sheet
class XLSX_Sheet(OBJ):
    '''
    XLSX Sheet
    -
    Contains the data required to create an individual sheet in an .xlsx file.

    Custom Attributes
    -
    - _data : `list[XLSX_Sheet._ROW]`
        - Collection of all data rows in the sheet. Each row contains a
            collection of unique column ids, and the cell data for each.
    - _headers : `dict[str, XLSX_Sheet._HEADER_POS]`
        - Collection of unique column ids, and the column number and header
            data for each.
    - _name : `str`
        - Name of the sheet.

    Custom Constants
    -
    - _HEADER_POS : `Type`
        - Custom Type Definition.
        - Current header in the sheet. Contains the position id and the header
            data.
    - _HEADER_NEW : `Type`
        - Custom Type Definition.
        - New header being added to the sheet. Contains only the id and header
            data as the position id will be automatically generated.
    - _ROW : `Type`
        - Custom Type Definition.
        - Single row in the sheet. Contains a collection of column ids and the
            associated cell data.

    Custom Methods
    -
    - __init__(name, headers=None, data=None) : `None`
        - Instance Method.
        - Creates a new sheet with the given name and content.
    - _get_data(lvl=0) : `OBJ._DATA`
        - `OBJ` Instance Method.
        - Produces a `dict` of keys and values of the data from the object.
    - add_header(header) : `None`
        - Instance Method.
        - Adds a new header to the sheet.
    - add_row(row) : `None`
        - Instance Method.
        - Adds a new row of data to the sheet.

    Custom Properties
    -
    - data : `list[XLSX_Sheet._ROW]`
        - Collection of all data rows in the sheet. Each row contains a
            collection of unique column ids, and the cell data for each.
    - headers : `dict[str, XLSX_Sheet._HEADER_POS]`
        - Collection of unique column ids, and the column number and header
            data for each.
    - name : `str`
        - Name of the sheet.
    '''

    # =========
    # Constants
    _HEADER_POS = Tuple[int, 'XLSX_Header']
    ''' Current header in the sheet. Contains the position id and the header
        data. '''
    _HEADER_NEW = Tuple[str, 'XLSX_Header']
    ''' New header being added to the sheet. Contains only the id and header
        data as the position id will be automatically generated. '''
    _ROW = Dict[str, str]
    ''' Single row in the sheet. Contains a collection of column ids and the
        associated cell data. '''

    # ===========
    # Constructor
    def __init__(
            self,
            name: str,
            headers: Optional[List[_HEADER_NEW]] = None,
            data: Optional[List[_ROW]] = None,
    ) -> None:
        # initialize rows data to empty
        self._data: List[XLSX_Sheet._ROW] = []
        ''' Collection of all data rows in the sheet. Each row contains a
            collection of unique column ids, and the cell data for each. '''

        # initialize headers data to empty
        self._headers: Dict[str, XLSX_Sheet._HEADER_POS] = {}
        ''' Collection of unique column ids, and the column number and header
            data for each. '''

        # set sheet name
        self._name: str = name
        ''' Name of the sheet. '''

        # add headers to the sheet
        if headers is not None:
            for header in headers: self.add_header(header)

        # add rows to the sheet
        if data is not None:
            for row in data: self.add_row(row)

    # ==========================
    # Property - Sheet Rows Data
    @property
    def data(self) -> List[_ROW]:
        ''' Collection of all data rows in the sheet. Each row contains a
            collection of unique column ids, and the cell data for each. '''
        return self._data

    # =============================
    # Property - Sheet Headers Data
    @property
    def headers(self) -> Dict[str, _HEADER_POS]:
        ''' Collection of unique column ids, and the column number and header
            data for each. '''
        return self._headers

    # =====================
    # Property - Sheet Name
    @property
    def name(self) -> str:
        ''' Name of the sheet. '''
        return self._name

    # =============
    # OBJ: Get Data
    def _get_data(self, lvl: int = 0) -> OBJ._DATA:
        # initialize data
        data = super()._get_data(lvl)

        # short representation
        if lvl == 0:
            data = {
                'name': self._name,
                '# headers': len(self._headers),
                '# rows': len(self._data),
            }

        # long representation / debug
        elif lvl in [1, 2]:
            data = {
                'name': self._name,
                'headers': self._headers,
                'data': self._data,
            }

        return data
    
    # ===================
    # Add Header to Sheet
    def add_header(self, header: _HEADER_NEW) -> None:
        '''
        Add Header to Sheet
        -
        Adds a new header to the sheet.

        Parameters
        -
        - header : `XLSX_Sheet._HEADER_NEW`
            - Header column ID + data.

        Returns
        -
        None
        '''

        # validate new header column id
        if header[0] in self.headers:
            raise PreExistingColumnID(f'New ID {header[0]} already exists')

        # create new header
        self._headers[header[0]] = (len(self.headers), header[1])

    # =====================
    # Add Data Row to Sheet
    def add_row(self, row: _ROW) -> None:
        '''
        Add Data Row to Sheet
        -
        Adds a new row of data to the sheet.

        Parameters
        -
        - row : `XLSX_Sheet._ROW`
            - Row column IDs + cell data.

        Returns
        -
        None
        '''

        # if the data row contains an ID that isn't in the header, then that
        #  particular cell's data will not be displayed in the sheet

        # add new row to data
        self._data.append(row)


# =============================================================================
# End of File
# =============================================================================
