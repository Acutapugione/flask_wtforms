from flask_wtf import Form, FlaskForm
from wtforms import StringField
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Length, NumberRange,
    URL, Email,
    ReadOnly, Optional, InputRequired, 
)  


class SearchForm(Form):
    text = StringField("Enter", validators=[])