from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.author import Author


@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def dojos():
    authors = Author.get_all()
    return render_template("index.html",all_authors = authors)


@app.route('/create/authors',methods=['POST'])
def create_author():
    Author.save(request.form)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def show_author(id):
    data = {
        "id": id
    }
    return render_template('author.html', authors=Author.get_one_with_books(data))
