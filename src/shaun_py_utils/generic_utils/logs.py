# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Generic - Loggers
-
Contains the definitions for implementing loggers within projects.

Contents
-
- get_logger(...) : `logging.Logger`
    - Creates a logger for a particular module within a project with the
        specified values.
    
Dependencies
-
- `concurrent_log_handler`
    - Used for creating a rotating file handler.
    - `concurrent-log-handler==0.9.25`
- `logging`
    - Used for creating / getting loggers.
    - Builtin.
- `typing`
    - Used for type hinting.
    - Builtin.

Internal Dependencies
-
None
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

# used for creating / getting loggers
import logging

# used for type hinting
from typing import (
    Optional, # optional data types
)


# =============================================================================
# Project / Module Logger Creator
# =============================================================================
def get_logger(
        log_name: Optional[str] = None,
        log_level: int = logging.DEBUG,
        log_dir: str = 'logs',
        log_file_name: str = 'log_app.log',
        log_format: str = '%(asctime)s [%(levelname)s] %(name)s - %(message)s',
        log_file_size: int = 1024 * 1024 * 10,
        log_backup_count: int = 5,
        log_propagate: bool = False
) -> logging.Logger:
    '''
    Project / Module Logger Creator
    -
    Creates a logger for a particular module within a project with the
    specified values.

    Parameters
    -
    - log_name : `str | None`
        - Name of the logger.
        - Defaults to `None`, meaning that the default root logger will be
            returned.
        - If specified, a new logger with this name will be created. If a
            logger with this name already exists, the existing logger will be
            returned instead.
    - log_level : `int`
        - Logging level of the logger.
        - Defaults to `logging.DEBUG` (`10`).
        - When the logger is used to log messages, it will only log messages if
            the `log_level` of the message is greater than or equal to this
            value.
    - log_dir : `str`
        - Folder within which to store the log files. Folder will be created in
            a position relative to the project root.
    - log_file_name : `str`
        - Name of the log files to be created within the log directory.
    - log_format : `str`
        - Format with which the log messages will be written.
        - Defaults to `%(asctime)s [%(levelname)s] %(name)s - %(message)s`,
            which outputs the date/time, log level, logger name, and log
            message.
        - For more information on the available format codes, see
            https://docs.python.org/3/library/logging.html.
    - log_file_size : `int`
        - Maximum file size to make log files. Once a log file reaches this
            size, its contents are rotated to the next log file in the
            sequence.
        - Defaults to `1024 * 1024 * 10`, which is 10MB.
    - log_backup_count : `int`
        - Number of back-up log files to maintain. When the data from a
            particular log file is rotated, it will go to `<log_name>.log.1`.
            The data that was in `<log_name>.log.1` will get moved to
            `<log_name>.log.2`, and so on. The maximum number of these back-up
            files is set by this parameter.
        - Defaults to `5`.
    - log_propagate : `bool`
        - Whether or not to propagate log messages recursively to all parents
            of the current logger. When `True`, all messages that are logged by
            the current logger will also be logged by the parent of the current
            logger + the grandparent of the current logger + etc. until the
            root logger (overarching parent of all loggers) is reached.
        - Defaults to `False`, meaning propagation is disabled.

    Returns
    -
    - `logging.Logger`
        - Logger for the specified module.
    '''

    # 3rd party package - used for creating a rotating file handler
    try:
        import concurrent_log_handler
    except:
        raise ImportError(
            'Failed to import `concurrent_log_handler` package. Please ' \
            + 'install using `pip install concurrent-log-handler`. The ' \
            + 'minimum required version is 0.9.20 (`pip install ' \
            + 'concurrent-log-handler==0.9.20`).'
        )

    # get the logger with the specified name
    l: logging.Logger = logging.getLogger(log_name)

    # set the logger level
    l.setLevel(log_level)

    # override the default logging propagation behaviour
    l.propagate = log_propagate

    # create the rotating file handler
    h = concurrent_log_handler.ConcurrentRotatingFileHandler(
        filename = f'{log_dir}/{log_file_name}',
        maxBytes = log_file_size,
        backupCount = log_backup_count
    )

    # set logger format
    h.setFormatter(logging.Formatter(log_format))

    # add the handler to the logger
    l.addHandler(h)

    # return the logger that was created
    return l


# =============================================================================
# End of File
# =============================================================================
