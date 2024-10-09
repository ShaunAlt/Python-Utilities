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
### 4. *Flask*
### 5. *Forms*
### 6. *Generic Functionality*
### 7. *SQLAlchemy*
### 8. *UI*
### 9. *XLSX*

## Usage

## Contributors



Awards Software + PGP Software - will both be run.
- Jason's replacement should know python - will be the back-end bug fixer.

PGP Software:
- Data import for Term 4. 


Awards:
- When normal staff have only a few classes - just immediately show them all of their classes.
    - If admin - have heirarchy. Else - just show the classes.