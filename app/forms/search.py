from flask_wtf import Form, FlaskForm
from wtforms import StringField, SubmitField
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


class SearchForm(Form):
    text = StringField(
        "Enter text to search",
        validators=[DataRequired("This is required field, my boy)")],
    )
    submit = SubmitField("Run searching")
