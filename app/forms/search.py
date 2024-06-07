from flask_wtf import Form, FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Length,
    NumberRange,
    URL,
    Email,
    ReadOnly,
    Optional,
    InputRequired,
)


class AnyForm(Form):
    text = StringField(
        "Enter text to search",
        validators=[
            DataRequired("This is required field, my boy)"),
            EqualTo("subtext", "Must be equal"),
            Length(min=10, max=15),
        ],
    )
    subtext = StringField("Repeat please")
    submit = SubmitField("Run searching")

    def validate_subtext(form, field):
        if field.data != "Mama mila ramu":
            raise ValidationError("subtext must be Mama mila ramu")
