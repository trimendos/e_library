from app import db

ROLES = {'user': 0,
         'admin': 1}


association_table = db.Table('association',
                             db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
                             db.Column('author_id', db.Integer, db.ForeignKey('authors.id')))


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    books = db.relationship('Book', secondary=association_table, back_populates="authors")

    def __init__(self, name=None, books=[]):
        self.name = name
        self.books = books

    def __str__(self):
        return '%s' % self.name


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    authors = db.relationship('Author', secondary=association_table, back_populates="books")

    def __init__(self, title=None, authors=[]):
        self.title = title
        self.authors = authors

    def __str__(self):
        return '%s' % self.title


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    # Required for administrative interface
    def __unicode__(self):
        return self.username
