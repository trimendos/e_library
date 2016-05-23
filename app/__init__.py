# import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# flask-admin
from flask.ext.admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

# flask-admin
admin = Admin(app)

app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

admin.add_view(ModelView(models.Author, session=db.session))
admin.add_view(ModelView(models.Book, session=db.session))

# logging.basicConfig()
# logging.getLogger('sql    alchemy.engine').setLevel(logging.INFO)