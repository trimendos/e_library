from flask_wtf import Form
from wtforms import BooleanField, TextField, PasswordField, validators, StringField, SelectField
from wtforms.validators import Required, DataRequired, Length


class SearchForm(Form):
    search = TextField('search', validators=[Required(), Length(min=3)])
    search_type = SelectField(u'Search type', choices=[('author', 'Author'),
                                                       ('book', 'Book')], default='book')
