from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.superadmin import Admin, model

app = Flask(__name__)
admin = Admin(app, 'Simple Models')


app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

admin.register(models.Author, session=db.session)
admin.register(models.Book, session=db.session)
# admin.register(User, session=db.session)