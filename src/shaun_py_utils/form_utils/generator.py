# =============================================================================
# Created By - Shaun Altmann
# =============================================================================
'''
Python Utilities - Forms - Field Generator
-
Contains the method used for dynamically creating form fields.

Contents
-
- create_field(...) : `wtforms.Field`
    - Creates a new WTForms field based on the specified parameters.

Dependencies
-
- `typing`
    - Used for type hinting.
    - Builtin.
- `wtforms`
    - Used for type hinting and creating the form fields.
    - `wtforms==3.1.2`.

Internal Dependencies
-
None
'''
# =============================================================================


# =============================================================================
# Imports
# =============================================================================

# used for type hinting
from typing import (
    Any, # any type
    List, # list type
    Optional, # optional type
    Type, # type hinted type
    TYPE_CHECKING, # static type checking flag
)

if TYPE_CHECKING:
    # used for type hinting wtforms fields
    from wtforms.fields import Field # type: ignore
else:
    Field = Any


# =============================================================================
# Form Field Generator
# =============================================================================
def create_field(
        field_type: Type[Field],
        field_label: Optional[str] = None,
        field_tooltip: Optional[str] = None,
        field_classes: Optional[List[str]] = None,
        field_placeholder: Optional[str] = None,
        field_required: bool = True,
        field_maxlength: Optional[int] = None,
        field_tall: bool = False,
        field_maxitems: Optional[int] = None,
        **kwargs: Any
) -> Field:
    '''
    Form Field Generator
    -
    Creates a new WTForms field based on the specified parameters.

    NOTE
    -
    - This method does not automatically add any `wtforms.validators`
        validation methods or objects to this field.
    - The `SelectField` and `SelectMultipleField` objects for this also make
        use of the SELECTIZE javascript library which simplifies searching and
        selection of items within these fields.

    Parameters
    -
    - field_type : `Type[Field]`
        - Type of field being generated.
        - Supported Types:
            - `wtforms.fields.BooleanField`
            - `wtforms.fields.ColorField`
            - `wtforms.fields.DateField`
            - `wtforms.fields.DateTimeField`
            - `wtforms.fields.DateTimeLocalField`
            - `wtforms.fields.DecimalField`
            - `wtforms.fields.DecimalRangeField`
            - `wtforms.fields.EmailField`
            - `wtforms.fields.FileField`
            - `wtforms.fields.FloatField`
            - `wtforms.fields.HiddenField`
            - `wtforms.fields.IntegerField`
            - `wtforms.fields.IntegerRangeField`
            - `wtforms.fields.MonthField`
            - `wtforms.fields.MultipleFileField`
            - `wtforms.fields.PasswordField`
            - `wtforms.fields.RadioField`
            - `wtforms.fields.SearchField`
            - `wtforms.fields.SelectField`
            - `wtforms.fields.SelectMultipleField`
            - `wtforms.fields.StringField`
            - `wtforms.fields.SubmitField`
            - `wtforms.fields.TelField`
            - `wtforms.fields.TextAreaField`
            - `wtforms.fields.TimeField`
            - `wtforms.fields.WeekField`
            - `wtforms.fields.URLField`
    - field_label : `str | None`
        - Label for the field being generated. Defaults to `None`, meaning no
            label will be created.
    - field_tooltip : `str | None`
        - Tooltip for the field being generated. Defaults to `None`, meaning to
            tooltip will be created. If set, the tooltip keyword arguments will
            be defined as used by Bootstrap 4.0.
    - field_classes : `list[str] | None`
        - Collection of classes to add to the generated field. Defaults to
            `None`, meaning no additional classes will be added to the field.
    - field_placeholder : `str | None`
        - Placeholder text for the generated field. Defaults to `None`, meaning
            no placeholder will be generated. If set, then when the field is
            empty, the placeholder text will be displayed.
    - field_required : `bool`
        - Flag for whether or not to set the field as being a "required" input.
            When `True`, indicates visually that the field requires an input.
    - field_maxlength : `int | None`
        - Only used with `StringField`, `TextAreaField`, and other text input
            fields. Used to create an attribute which indicates the maximum
            number of characters that can be entered. Defaults to `None`,
            meaning no maximum length will be set.
    - field_tall : `bool`
        - Flag for whether or not to add a `tall-input` class to the field,
            making it default to being a taller, multi-line input field.
    - field_maxitems : `int | None`
        - Only used with `SelectMultipleField`. Used to create an attribute
            which indicates the maximum number of items that can be selecetd in
            the field. Defaults to `None`, meaning no maximum number will be
            set.
    - **kwargs : `Any`
        - Additional keyword arguments that will be passed as additional
            attributes to the input field when rendered.

    Returns
    -
    - `Field`
        - Field instance created from the given parameter data.
    '''

    # import field types
    try:
        from wtforms.fields import (
            BooleanField,
            ColorField,
            DateField,
            DateTimeField,
            DateTimeLocalField,
            DecimalField,
            DecimalRangeField,
            EmailField,
            FileField,
            FloatField,
            HiddenField,
            IntegerField,
            IntegerRangeField,
            MonthField,
            MultipleFileField,
            PasswordField,
            RadioField,
            SearchField,
            SelectField,
            SelectMultipleField,
            StringField,
            SubmitField,
            TelField,
            TextAreaField,
            TimeField,
            WeekField,
            URLField,
        )
    except:
        raise ImportError(
            'Failed to import the `wtforms` package. Please install using ' \
            + '`pip install wtforms`. The minimum required version is 3.1.2 ' \
            + '(`pip install wtforms==3.1.2`).'
        )

    # setting main render-keyword arguments
    kwargs['required'] = field_required
    kwargs['class'] = '' if field_classes is None else ' '.join(field_classes)

    # setting tooltip arguments
    if field_tooltip is not None:
        kwargs['data-toggle'] = 'tooltip'
        kwargs['data-placement'] = 'top'
        kwargs['data-bss-toggle'] = True
        kwargs['title'] = field_tooltip

    # setting optional render-keyword arguments
    if field_tall: kwargs['class'] += ' tall-input'
    if field_maxlength is not None: kwargs['max-length'] = field_maxlength
    if field_placeholder is not None: kwargs['placeholder'] = field_placeholder
    if field_maxitems is not None: kwargs['max-items'] = field_maxitems

    # create field
    if field_type is BooleanField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is ColorField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is DateField:
        kwargs['type'] = 'date'
        return field_type(field_label, render_kw = kwargs)
    elif field_type is DateTimeField:
        kwargs['type'] = 'datetime-local'
        return field_type(field_label, render_kw = kwargs)
    elif field_type is DateTimeLocalField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is DecimalField:
        kwargs['type'] = 'number'
        kwargs['step'] = 'any'
        return field_type(field_label, render_kw = kwargs)
    elif field_type is DecimalRangeField:
        kwargs['step'] = 'any'
        return field_type(field_label, render_kw = kwargs)
    elif field_type is EmailField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is FileField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is FloatField:
        kwargs['type'] = 'number'
        kwargs['step'] = 'any'
        return field_type(field_label, render_kw = kwargs)
    elif field_type is HiddenField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is IntegerField:
        kwargs['type'] = 'number'
        kwargs['step'] = '1'
        return field_type(field_label, render_kw = kwargs)
    elif field_type is IntegerRangeField:
        kwargs['step'] = '1'
        return field_type(field_label, render_kw = kwargs)
    elif field_type is MonthField:
        kwargs['type'] = 'date'
        return field_type(field_label, render_kw = kwargs)
    elif field_type is MultipleFileField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is PasswordField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is RadioField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is SearchField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is SelectField:
        kwargs['selectize'] = 'single'
        return field_type(field_label, render_kw = kwargs)
    elif field_type is SelectMultipleField:
        kwargs['selectize'] = 'multi'
        return field_type(field_label, render_kw = kwargs)
    elif field_type is StringField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is SubmitField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is TelField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is TextAreaField:
        return field_type(field_label, render_kw = kwargs)
    elif field_type is TimeField:
        kwargs['type'] = 'time'
        return field_type(field_label, render_kw = kwargs)
    elif field_type is WeekField:
        kwargs['type'] = 'date'
        return field_type(field_label, render_kw = kwargs)
    elif field_type is URLField:
        return field_type(field_label, render_kw = kwargs)
    
    # invalid field type
    raise TypeError(f'Invalid Field Type = {field_type!r}')
    


# =============================================================================
# End of File
# =============================================================================
