from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import author, book

@app.route('/books')
def books():
    
    return render_template('book.html',authors= author.Author.get_all())


@app.route('/create/books',methods=['POST'])
def create_book():
    book.Book.save(request.form)
    return redirect('/')