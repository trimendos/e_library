import json

from app import app
from forms import SearchForm
from flask import render_template, flash, redirect, session, url_for, request, g
from models import Author, Book


@app.route('/')
@app.route('/index')
def index():
    search_form = SearchForm()
    return render_template('index.html', title='Home', search_form=search_form)


@app.route('/searchResult', methods=['POST'])
def searchResult():
    form = SearchForm(request.form)
    key_word = request.form['search']
    search_type = request.form['search_type']
    if request.method == 'POST' and form.validate():
        books = False
        if search_type == 'book':
            books = Book.query.filter(Book.title.like("%{0}%".format(key_word))).all()
            data = [{'title': book.title,
                     'authors': [author.name for author in book.authors] if book.authors else []} for book in books]

        elif search_type == 'author':
            books = Author.query.filter(Author.name.like("%{0}%".format(key_word))).all()
            data = [{'name': i.name,
                     'books': [book.title for book in i.books] if i.books else []} for i in books]

        if books:
            return json.dumps({'search_type': search_type, 'data': data})

        return json.dumps({'message': 'No matches found'})
    return json.dumps({'errors': form.errors})
