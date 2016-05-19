from app import app
from forms import SearchForm
from flask import render_template, flash, redirect, session, url_for, request, g
from models import Author


@app.route('/')
@app.route('/index')
def index():
    search_form = SearchForm()
    return render_template('index.html', title='Home', search_form=search_form)


@app.route('/search', methods = ['POST'])
# @login_required
def search():
    if not search_form.validate_on_submit():
        return redirect(url_for('index'))
    return redirect(url_for('search_results'))#, query=search_form.search.data))


@app.route('/signUp')
def signUp():
    return render_template('signUp.html')


import json


@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user = request.form['username']
    password = request.form['password']
    return json.dumps({'status': 'OK', 'user': user, 'pass': password})


@app.route('/searchResult', methods=['POST'])
def searchResult():
    search = request.form['search']
    data_from_db = """<h4>Subheading</h4><p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>"""
    return json.dumps({'status': 'OK', 'search': search, "data_from_db": data_from_db})
