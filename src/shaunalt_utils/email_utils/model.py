# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Emails - Email Model
-
Contains the definition of the main email object that stores all of the
information required to create a new email message.

Contents
-
- `Email`
    - Represents an individual email that can be sent to specified addresses,
        containing the given data.

Dependencies
-
- `email`
    - Used for creating email messages.
    - Builtin.
- `io`
    - Used for storing raw file content.
    - Builtin.
- `logging`
    - Used for creating / getting loggers.
    - Builtin.
- `mimetypes`
    - Used for creating mimetypes for common file types.
    - Builtin.
- `smtplib`
    - Used for connecting to the SMTP server.
    - Builtin.
- `typing`
    - Used for type hinting.
    - Builtin.

Internal Dependencies
-
- `generic_utils`
    - Used for base object definition.
    - `generic_utils`.
- `.errors`
    - Used for custom exceptions.
    - `email_utils.errors`.
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

# used for base object
from ..generic_utils import OBJ

# used for custom exceptions
from .errors import (
    InvalidAttachmentError,
)

# used for encoding email attachments
from email import encoders

# used for creating email attachments
from email.mime.base import MIMEBase

# used for creating email content
from email.mime.multipart import MIMEMultipart

# used for creating email html formatted content
from email.mime.text import MIMEText

# used for storing raw file content
from io import BytesIO

# used for logging email data
import logging

# used for creating mimetypes for common file types
import mimetypes

# used for connecting to the SMTP server
import smtplib

# used for type hinting
from typing import (
    Dict, # dict type
    List, # list type
    Optional, # optional type
    Tuple, # tuple type
)


# =============================================================================
# Email Model Definition
# =============================================================================
class Email(OBJ):
    '''
    Email Model
    -
    Represents an individual email that can be sent to specified addresses,
    containing the given data.

    Custom Attributes
    -
    - _attachments : `list[Tuple[str, BytesIO]]`
        - Collection of all attachment files (name + data) to add to the email
            when being sent.
    - _bcc : `list[str]`
        - Collection of email addresses to add to the "BCC" section of the
            email when being sent.
    - _cc : `list[str]`
        - Collection of email addresses to add to the "CC" section of the email
            when being sent.
    - _html : `str`
        - Fully rendered html that will be sent as the body of the email.
    - _logger : `logging.Logger`
        - Logger used for logging all email attempts to an email log file.
    - _subject : `str`
        - Single line subject line for the email when being sent.
    - _to : `list[str]`
        - Collection of email addresses to add to the "To" section of the email
            when being sent.

    Custom Constants
    -
    - FILETYPES : `dict[str, str]`
        - Collection of additional file types, and the required mime type for
            each.

    Custom Methods
    -
    - __init__(to, subject, html, bcc=None, cc=None) : `None`
        - Instance Method.
        - Initializes the email object with the given recipient(s), subject,
            and HTML content.
    - _convert_attachment(file_name, file_data) : `MIMEBase`
        - Instance Method.
        - Converts an attachment file to a `MIMEBase` object which can be
            attached to an email message.
    - _get_data(lvl=0) : `_OBJ.DATA`
        - `OBJ` Instance Method.
        - Produces a `dict` of keys and values of the data from the object.
    - _to_msg(smtp_sender, bounce_address=None) : `MIMEMultipart`
        - Instance Method.
        - Converts the email object into an `MIMEMultipart` object that can be
            sent through the `SMTP` object.
    - add_attachment(file_name, file_data, max_size=5MB) : `bool`
        - Instance Method.
        - Attempts to add an attachment to the email object with the given
            file name and file data.
    - send(smtp_server, smtp_port, smtp_sender, bounce_address=None) : `bool`
        - Instance Method.
        - Attempts to send the email object through the specified SMTP server
            and port, and from the specified sender address.

    Custom Properties
    -
    - recipients : `list[str]`
        - Collection of all recipients of the email when being sent (`to` + 
            `cc` + `bcc`).
    '''

    # =========
    # Constants
    FILETYPES = {
        '.xlsx': (
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        ),
    }

    # ===========
    # Constructor
    def __init__(
            self,
            to: List[str],
            subject: str,
            html: str,
            logger: logging.Logger,
            bcc: Optional[List[str]] = None,
            cc: Optional[List[str]] = None
    ) -> None:
        # set attachments list
        self._attachments: List[Tuple[str, BytesIO]] = []
        ''' Collection of all attachment files (name + data) to add to the
            email when being sent. '''
        
        # set 'BCC' recipients list
        self._bcc: List[str] = [] if bcc is None else bcc
        ''' Collection of email addresses to add to the "BCC" section of the
            email when being sent. '''

        # set 'CC' recipients list
        self._cc: List[str] = [] if cc is None else cc
        ''' Collection of emails addresses to add to the "CC" section of the
            email when being sent. '''

        # set email body html content
        self._html: str = html
        ''' Fully rendered html that will be sent as the body of the email. '''

        # set email logger
        self._logger: logging.Logger = logger
        ''' Logger used for logging all email attempts to an email log
            file. '''

        # set email subject line
        self._subject: str = subject
        ''' Single line subject line for the email when being sent. '''

        # set 'To' recipients list
        self._to: List[str] = to
        ''' Collection of email addresses to add to the "To" section of the
            email when being sent. '''
        
    # ==========================
    # Property - Recipients List
    @property
    def recipients(self) -> List[str]:
        ''' Collection of all recipients of the email when being sent (`to` + 
            `cc` + `bcc`). '''
        
        # use list(set(...)) to remove duplicates but still keep the list type
        return list(set(self._to + self._cc + self._bcc))
    
    # ===========================
    # Convert Attachment Datatype
    def _convert_attachment(
            self,
            file_name: str,
            file_data: BytesIO
    ) -> MIMEBase:
        '''
        Convert Attachment Datatype
        -
        Converts an attachment file to a `MIMEBase` object which can be
        attached to an email message.

        Parameters
        -
        - file_name : `str`
            - Name of the file being attached.
        - file_data : `BytesIO`
            - Raw data of the file being attached.

        Returns
        -
        - `MIMEBase`
            - Attachment file converted into a datatype acceptable for being
                attached to the email message.
        '''

        # initialize variables
        attachment: MIMEBase # attachment object being created from the file
        mime_type: Optional[str] = None # mimetype of the attachment file

        # identify mimetype from file name
        _, mime_type = mimetypes.guess_type(file_name) # check common types
        if ( # if not found - check custom defined types
                (mime_type is None)
                and (file_name.split('.')[-1] in Email.FILETYPES)
        ):
            mime_type = Email.FILETYPES[file_name.split('.')[-1]]

        # validate mimetype
        if (mime_type is None) or (len(mime_type.split('/')) != 2):
            raise InvalidAttachmentError(file_name)

        # create attachment object from file data
        attachment = MIMEBase(
            _maintype = mime_type.split('/')[0],
            _subtype = mime_type.split('/')[1]
        )
        file_data.seek(0)
        attachment.set_payload(file_data.read())
        encoders.encode_base64(attachment)
        attachment.add_header(
            _name = 'Content-Disposition',
            _value = f'attachment; filename="{file_name}"'
        )

        # return attachment object
        return attachment
    
    # =============
    # OBJ: Get Data
    def _get_data(self, lvl: int = 0) -> OBJ._DATA:
        # initialize data
        data = super()._get_data(lvl)

        # short representation
        if lvl == 0:
            data = {
                'subject': self._subject,
            }
        
        # long representation
        elif lvl == 1:
            data = {
                'attachments': [filename for filename, _ in self._attachments],
                'bcc': self._bcc,
                'cc': self._cc,
                'subject': self._subject,
                'to': self._to,
            }
        
        # debug representation
        elif lvl == 2:
            data = {
                '_attachments': self._attachments,
                '_bcc': self._bcc,
                '_cc': self._cc,
                '_html': self._html,
                '_logger': self._logger,
                '_subject': self._subject,
                '_to': self._to,
                'recipients': self.recipients,
            }

        return data

    # ====================
    # Create Email Message
    def _to_msg(
            self,
            smtp_sender: str,
            bounce_address: Optional[str] = None
    ) -> MIMEMultipart:
        '''
        Create Email Message
        -
        Converts the email object into an `MIMEMultipart` object that can be
        sent through the `SMTP` object.

        Parameters
        -
        - smtp_sender : `str`
            - Email address from which to send the email.
        - bounce_address : `str | None`
            - Defaults to `None`, meaning bounced emails will not be
                redirected. If set, then all bounced emails will be redirected
                to the provided email.

        Returns
        -
        - `MIMEMultipart`
            - Object that can be sent by the smtp server.
        '''

        # create base message
        msg = MIMEMultipart()

        # define sender + recipients
        msg['From'] = smtp_sender
        msg['To'] = ', '.join(self._to)
        if len(self._cc) > 0: msg['Cc'] = ', '.join(self._cc)
        if len(self._bcc) > 0: msg['Bcc'] = ', '.join(self._bcc)

        # set bounce address
        if bounce_address is not None: msg['Return-Path'] = bounce_address

        # set email subject
        msg['Subject'] = self._subject

        # set email body content
        msg.attach(MIMEText(self._html, 'html'))

        # add email attachments
        for file_name, file_data in self._attachments:
            msg.attach(self._convert_attachment(file_name, file_data))

        return msg

    # =======================
    # Add Attachment to Email
    def add_attachment(
            self,
            file_name: str,
            file_data: BytesIO,
            max_size: int = 1024 * 1024 * 5
    ) -> bool:
        '''
        Add Attachment to Email
        -
        Attempts to add an attachment to the email object with the given
        file name and file data.

        If the file attachment is too big, of an invalid datatype, etc. then it
        will return `False` and not add the attachment to the email.

        Parameters
        -
        - file_name : `str`
            - Name of the file being attached.
        - file_data : `BytesIO`
            - Raw data of the file being attached.
        - max_size : `int`
            - Maximum combined file size for all attachments. Defaults to 5MB.

        Returns
        -
        - `bool`
            - Whether or not the file was able to be added to the email.
        '''

        # initialize variables
        mime_type: Optional[str] = None # mimetype of the attachment file

        # identify mimetype from file name
        _, mime_type = mimetypes.guess_type(file_name) # check common types
        if ( # if not found - check custom defined types
                (mime_type is None)
                and (file_name.split('.')[-1] in Email.FILETYPES)
        ):
            mime_type = Email.FILETYPES[file_name.split('.')[-1]]

        # validate mimetype
        if (mime_type is None) or (len(mime_type.split('/')) != 2):
            return False
        
        # validate file data size
        if (
                len(file_data.getbuffer()) > (
                    max_size \
                    - sum([
                        len(f_data.getbuffer())
                        for _, f_data in self._attachments
                    ])
                )
        ):
            return False

        # add attachment to attachments list
        self._attachments.append((file_name, file_data))

        return True

    # ==========
    # Send Email
    def send(
            self,
            smtp_server: str,
            smtp_port: int,
            smtp_sender: str,
            bounce_address: Optional[str] = None
    ) -> bool:
        '''
        Send Email
        -
        Attempts to send the email object through the specified SMTP server
        and port, and from the specified sender address.

        Parameters
        -
        - smtp_server : `str`
            - Server to send the email through.
        - smtp_port : `int`
            - Port to send the email through.
        - smtp_sender : `str`
            - Email address from which to send the email.
        - bounce_address : `str | None`
            - Defaults to `None`, meaning bounced emails will not be
                redirected. If set, then all bounced emails will be redirected
                to the provided email.

        Returns
        -
        - `bool`
            - Whether or not the email was able to be sent.
        '''

        # initialize variables
        bounces: Dict[str, Tuple[int, bytes]] # collection of failed sends
        msg: MIMEMultipart # email message to send

        try:
            # create email message
            msg = self._to_msg(smtp_sender, bounce_address)

            # send email using smtplib
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                # send email
                bounces = server.sendmail(
                    from_addr = smtp_sender,
                    to_addrs = self.recipients,
                    msg = msg.as_string()
                )

            # log success/failure
            if len(bounces) == 0:
                self._logger.info(f'Successfully Sent Email: {self!r}')
            else:
                self._logger.warning(
                    f'Sent Email with Bounces: {bounces}, {self!r}'
                )
            
            # return success
            return True
        except Exception as e:
            self._logger.error(f'Failed to Send Email {e}', exc_info = True)

        # if failed to create/send - return failure
        return False


# =============================================================================
# End of File
# =============================================================================
