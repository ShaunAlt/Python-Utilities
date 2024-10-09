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
    - Route Error Handler
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
    - Method Timer
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
- Email Model
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
- Error Handler
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
- Field Generator
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
### 7. *SQLAlchemy*
### 8. *UI*
### 9. *XLSX*
- XLSX Models
    - XLSX Book
        - Contains the data required to create an individual .xlsx workbook
            file.
    - XLSX Header
        - Contains the data for a single column header in an .xlsx sheet.
    - XLSX Sheet
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
        book.add_sheet(new_sheet = sheet)

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