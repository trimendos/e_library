from app import db

ROLES = {'user': 0,
         'admin': 1}


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    author = db.relationship('Item', backref='Book', lazy='dynamic')


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    book = db.relationship('Item', backref='Author', lazy='dynamic')


class Item(db.Model):
    book_id = db.Column(db.Integer, db.ForeignKey('Book.id'), primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('Author.id'), primary_key=True)