# Python-Utilities
Contains a collection of various Python objects and methods that can be used to
simplify the functionality of Flask web-based applications.

## Table of Contents

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