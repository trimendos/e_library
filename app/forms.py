from flask_wtf import Form
from wtforms import BooleanField, TextField, PasswordField, validators, StringField
from wtforms.validators import Required, DataRequired


class SearchForm(Form):
    search = TextField('search', validators=[Required()])
