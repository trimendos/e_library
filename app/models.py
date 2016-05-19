from app import db, app
import flask_whooshalchemy as whooshalchemy

ROLES = {'user': 0,
         'admin': 1}


association_table = db.Table('association',
                             db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
                             db.Column('author_id', db.Integer, db.ForeignKey('authors.id')))


class Author(db.Model):
    __tablename__ = 'authors'
    __searchable__ = ['name']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    books = db.relationship('Book', secondary=association_table, back_populates="authors")

    def __repr__(self):
        return '<Author %r>' % self.name


class Book(db.Model):
    __tablename__ = 'books'
    __searchable__ = ['title']

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    authors = db.relationship('Author', secondary=association_table, back_populates="books")

    def __repr__(self):
        return '<Book %r>' % self.title

whooshalchemy.whoosh_index(app, Book)
whooshalchemy.whoosh_index(app, Author)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    # Required for administrative interface
    def __unicode__(self):
        return self.username


# class Item(db.Model):
#     book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
#     author_id = db.Column(db.Integer, db.ForeignKey('author.id'), primary_key=True)


# book = models.Book(title='Black Hat Python', author='Justin Seitz')
# author = models.Author(name='Justin Seitz')
# from app import db, models