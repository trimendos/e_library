import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'e-library.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
MAX_SEARCH_RESULTS = 50
WHOOSH_BASE = os.path.join(basedir, 'search.db')
