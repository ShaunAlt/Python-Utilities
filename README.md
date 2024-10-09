# Python-Utilities
Contains a collection of various Python objects and methods that can be used to
simplify the functionality of Flask web-based applications.

## Table of Contents
- [Features](#features)
    - [1. Decorators](#1-decorators)
    - [2. Emails](#2-emails)
    - [3. Error Handling](#3-error-handling)
    - [4. Flask](#4-flask)
    - [5. Forms](#5-forms)
    - [6. Generic Functionality](#6-generic-functionality)
    - [7. SQLAlchemy](#7-sqlalchemy)
    - [8. UI](#8-ui)
    - [9. XLSX](#9-xlsx)
- [Usage](#usage)
- [Contributors](#contributors)

## Features
### 1. *Decorators*
Contains a collection of various method decorators that can be used simplify
particular application methods.

Includes:
- Flask Method Decorators
    - Route Error Handler (`flask_error_handler`)
        - Wraps the decorated function in a `try / except` statement. If an
            error occurs, the decorator will handle the error that occurred. If
            the error was a `werkzeug.exceptions.HTTPException` (raised by
            `flask.abort`), the decorator will allow the error to be raised so
            that `flask` can handle it appropriately. Otherwise, the decorator
            will store the type of error that occurred, the name of the
            decorated function, the `flask_login.current_user`, and the
            `flask.request` data. If the decorator is given a method that will
            allow it to create an `email_utils.Email` object, this will be
            created and sent. The decorator will finish by raising a
            `flask.abort` error that `flask` will then be expected to handle.
        - Implementation Example:
            ``` python
            # imports that would be required in a flask application / blueprint
            # module
            import logging
            import flask

            # flask application
            app = flask.Flask(__name__)

            # logger used to logging flask route errors
            log = logging.getLogger('flask_error_handler')

            # test flask route
            @app.route('/test') # flask route handler
            @flask_error_handler(log) # flask error handler decorator
            def test():
                raise ValueError('foo')
            ```
- Generic Method Decorators
    - Method Timer (`method_timer`)
        - Wraps the decorated function within a `generic_utils.TIMER` object
            that will time the overall method.
        - Implementation Example:
            ``` python
            # imports that would be required in a module for timing + logging
            import logging
            from generic_utils import TIMER

            # logger used to log the timer
            log = logging.getLogger('method_timer')

            # function that will be timed
            @method_timer(log)
            def timed_function():
                return 'hello world!'
            ```

### 2. *Emails*
- Email Model (`Email`)
    - Represents an individual email that can be sent to specified email
        addresses, containing the given data.
    - Implementation Example:
        ``` python
        # import email model
        from email_utils import Email

        # import io for in-memory file handling
        import io

        # import module logger
        import logging

        # create module logger
        log = logging.getLogger('email model')

        # create email object
        new_email = Email(
            to = ['foo@bar.com',],
            subject = 'Test Subject Line',
            html = '<h1>Hello World</h1><h2>Another test line</h2>',
            logger = log,
            bcc = None,
            cc = ['bar@foo.com',]
        )

        # add attachments to the email
        attachment_added = new_email.add_attachment(
            file_name = 'test.pdf',
            file_data = io.BytesIO()
        )

        # send email
        email_sent_successfully = new_email.send(
            smtp_server = 'SMTP Server Name',
            smtp_port = 0,
            smtp_sender = 'from@foo.bar.com',
            bounce_address = 'bounce@foo.bar.com'
        )
        ```

### 3. *Error Handling*
- Error Handler (`error_handler`)
    - Creates a new `Exception` containing all of the keyword and error
        description data parsed. The purpose of this is to simplify the
        creation of an `Exception` object when the developer wishes to parse
        keyword information through (e.g. variables that could have been a 
        factor in causing the exception to be thrown).
    - Implementation Example:
        ``` python
        # import error handler
        from error_utils import error_handler

        # import module logger creator
        import logging

        # create module logger
        log = logger.getLogger('error handler')

        # function to divide values
        def divide(a, b):
            try:
                return a / b
            except:
                raise error_handler(
                    e = ValueError,
                    desc = 'Unable to divide the values',
                    log = log,
                    a = a, # keyword argument
                    b = b # keyword argument
                )
        ```

### 4. *Flask*
- Not Yet Implemented.

### 5. *Forms*
- Field Generator (`create_field`)
    - Creates a new `wtforms.fields.Field` object containing templated keyword
        arguments and attributes based on specified parameters.
    - Implementation Example 1:
        ``` python
        # import the field generator
        from form_utils import create_field

        # import the wtforms field being created
        from wtforms.fields import SubmitField

        # create new "submit" button field
        fld_submit = create_field(
            field_type = SubmitField,
            field_label = "Submit",
            field_tooltip = "Submit the Current Data",
            field_classes = ["form-button", "form-submit",]
        )
        ```
    - Implementation Example 2:
        ``` python
        # import field generator
        from form_utils import create_field

        # import the wtforms field being created
        from wtforms.field import StringField

        # create new "name" input field that will run a javascript `submit()`
        # function
        fld_name = create_field(
            field_type = StringField,
            field_label = "Name:",
            field_tooltip = "Input the Name Here",
            field_placeholder = "Name ...",
            field_required = False,
            field_maxlength = 100,
            onclick = "submit()"
        )
        ```

### 6. *Generic Functionality*
- Logger Generator (`get_logger`)
    - Creates a logger for a particular module within a project with the
        specified values.
    - Implementation Example:
        ``` python
        # import logger generator
        from generic_utils import get_logger as _get_logger

        # create customized logger generator with optional specialisations
        def get_logger(
                log_name = None,
                error_logger = False,
                timer_logger = False
        ):
            # override to create special error handler logger
            if error_logger:
                return _get_logger(
                    "ERROR HANDLER",
                    ...
                )

            # override to create special timing logger
            if timer_logger:
                return _get_logger(
                    "TIMING LOGGER",
                    ...
                )

            # create normal logger
            return _get_logger(
                log_name,
                ...
            )

        # create various application loggers
        log_normal = get_logger(__name__) # module logger
        log_error = get_logger(error_logger = True) # error handler logger
        log_timer = get_logger(timer_logger = True) # timer logger
        ```
- Base Object Definition (`OBJ`)
    - Represents a base object with generic functionality that all other
        objects can inherit from. It contains a lot of debugging and other
        functionality that can easily be extended in child classes, effectively
        providing a standardized base that all application objects can derive
        from.
    - Implementation Example:
        ``` python
        # import base object definition
        from generic_utils import OBJ

        # create custom object that will potentially require debugging etc.
        class New_Class(OBJ):
            ...
        ```
- Code Timer Object (`TIMER`)
    - Used for timing sections of code, measuring the elapsed time in
        nanoseconds. Can be used to help identify sections of code that are
        causing lagging issues.
    - Implementation Example:
        ``` python
        # import code timer object
        from generic_utils import TIMER

        # create function that will require timing
        def test_function():
            # create timer
            t = TIMER(...)

            # time various sections
            with t.lap('Part 1 to time'):
                pass

            # time with indentation
            with t.lap('Part 2 to time'):
                with t.lap('Part 2.1'):
                    pass
                with t.lap('Part 2.2'):
                    pass

            return # timer will automatically stop itself with __del__
        ```

### 7. *SQLAlchemy*
- Not Yet Implemented.

### 8. *UI*
- Navigation Menu Models
    - Base Navigation Object (`UI_Nav_OBJ`)
        - Base class for navigation menu objects, containing all of the shared
            functionality they require.
    - Navigation Button (`UI_Nav_Button`)
        - Individual button in the navigation menu that can be used to go to a
            specific route.
    - Navigation Dropdown (`UI_Nav_Dropdown`)
        - Dropdown menu that can be used to either contain a pre-loaded set of
            child navigation menu objects, or a route to lazy-load children
            from.
    - Implementation Example:
        ``` python
        # importing flask to create dynamic routes
        from flask import url_for

        # importing navigation menu objects
        from ui_utils import UI_Nav_Button, UI_Nav_Dropdown

        # creating navigation menu
        nav_menu = UI_Nav_Dropdown( # overall navigation menu dropdown
            label = "Application Menu",
            children = [ # pre-loaded children
                UI_Nav_Button(
                    label = "Home Page",
                    route = url_for("index"),
                    current = True, # current page identifier
                    icon = "fas fa-user", # FontAwesome free icon
                    border_bottom = True, # border flag for bottom of button
                    tooltip = "Go to Home Page"
                ),
                UI_Nav_Dropdown(
                    label = "Other Content",
                    route = url_for("nav_other_content") # lazy-load children
                )
            ]
        )
        ```
- Page Model (`UI_Page`)
    - Contains the data required to create a dynamic web-page in the user
        interface. Specific applications should create a child class that
        inherits all of the functionality of this model but defines custom
        implementations specific to the individual application.
    - Implementation Example:
        ``` python
        # import flask template rendering
        from flask import render_template

        # import ui page original definition
        from ui_utils import UI_Page

        # create new page object
        class NEW_Page(UI_Page):
            def __init__(
                self,
                title,
                code = None,
                forms = None,
                tables = None,
                title_prefix = 'Application Name'
            ):
                super().__init__(title, code, forms, tables, title_prefix)

            def create_nav(self, _time = -1):
                # create the dynamic navigation menu here
                self.nav = []

            def render(self, html, _time = -1, **kwargs):
                # complete any last-minute page data handling
                self.create_nav() # create navigation menu if not already done

                # render template
                try:
                    return render_template(html, page = self, **kwargs)
                except:
                    raise RuntimeError("Unable to render page")
        ```
- Table Models
    - Overall Table Model (`UI_Table`)
        - Contains the data required to create a table in the user interface.
    - Table Buttons Collection (`UI_Table_Btns`)
        - Contains a collection of flags that can be used to indicate which
            buttons should be displayed in a table or table row.
    - Table Data Row (`UI_Table_Row`)
        - Contains a single row of data for the table.
    - Implementation Example:
        ``` python
        # import flask url creation functionality
        from flask import url_for

        # import table models
        from ui_utils import UI_Table, UI_Table_Btns, UI_Table_Row

        # create new ui table
        t = UI_Table(
            title = "Table Title",
            desc = "This is a nice description of the table",
            headers = [
                ("Col 1", 1),
                ("Col 2", 1),
                ("Col 3", 2), # this header spans 2 columns
            ],
            rows = [ # table data rows
                UI_Table_Row(
                    id = "row0",
                    cells = [
                        ("cell 0.0", 1),
                        ("cell 0.1", 1),
                        ("cell 0.2.0", 1),
                        ("cell 0.2.1", 1),
                    ],
                    btns = UI_Table_Btns( # collection of which buttons to show
                        flag_edit = True,
                        flag_view = True
                    ),
                    route_func = (
                        lambda x: url_for(
                            "table_button_handler",
                            button_type = x
                        )
                    ),
                    children = None,
                    depth = 0
                )
            ],
            btns_add = [
                ( # list of multiple "Add" buttons
                    "New Folder", # label
                    url_for("new_folder"), # route
                    "Create a New Folder", # tooltip
                ),
                ("New Item", url_for("new_item"), "Create a New Item",)
            ],
            btns_download = None, # download button (same format as "Add")
            search = url_for("search_htmx"), # route for handling search input
            form = None # data filtering form
        )
        ```

### 9. *XLSX*
- XLSX Models
    - XLSX Book (`XLSX_Book`)
        - Contains the data required to create an individual .xlsx workbook
            file.
    - XLSX Sheet Header (`XLSX_Header`)
        - Contains the data for a single column header in an .xlsx sheet.
    - XLSX Sheet (`XLSX_Sheet`)
        - Contains the data required to create an individual sheet within an
            .xlsx file.
    - Implementation Example:
        ``` python
        # import xlsx sheet and header model
        from xlsx_utils import XLSX_Book, XLSX_Header, XLSX_Sheet

        # create all of the headers for a single sheet
        headers = ( # list of tuple is used instead of dict to preserve order
            (
                "col1", # column id
                XLSX_Header(label = "Header 1", width = 20), # header data
            ),
            (
                "col2",
                XLSX_Header(label = "Header 2", width = 30),
            ),
        )

        # create all of the data for a single sheet
        data = [ # list of dicts is used to preserve order of data rows
            {
                "col1": "hello", # row 0, "col1" cell value
                "col2": "world",
            },
            {
                "col2": "bar", # order doesn't matter because of column ids
                "col1": "foo",
            },
        ]

        # create an xlsx sheet
        sheet = XLSX_Sheet(name = "Sheet 1", headers = headers, data = data)

        # add another header to the sheet
        sheet.add_header((
            "col3",
            XLSX_Header("Another Header", 50),
        ))

        # add another row of data to the sheet
        sheet.add_row({
            "col1": "will show in col1",
            "col3": "will show in col3",
            "col5": "no matching column id, so will not get displayed",
        })

        # create a new xlsx workbook
        book = XLSX_Book(sheets = [sheet])
        book.add_sheet(new_sheet = sheet) # add the sheet again

        # create an `io.BytesIO` object to store the file in-memory
        file = book.create()

        '''
        Sheet Data Overview
        +- (20 wide) -+- (30 wide) -+- (50 wide) -+
        | Header 1    | Header 2    | Header 3    |
        |-------------+-------------+-------------|
        | hello       | world       |             |
        |-------------+-------------+-------------|
        | foo         | bar         |             |
        |-------------+-------------+-------------|
        | will show   |             | will show   |
        | in col1     |             | in col3     |
        |-------------+-------------+-------------|
        '''
        ```

## Usage

## Contributors



Awards Software + PGP Software - will both be run.
- Jason's replacement should know python - will be the back-end bug fixer.

PGP Software:
- Data import for Term 4. 


Awards:
- When normal staff have only a few classes - just immediately show them all of their classes.
    - If admin - have heirarchy. Else - just show the classes.