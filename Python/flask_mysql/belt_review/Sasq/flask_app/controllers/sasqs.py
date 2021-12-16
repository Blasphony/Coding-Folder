from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.sasq import Sasq
from flask_app.models.user import User


@app.route('/new/sasq')
def new_sasq():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_sasq.html',user=User.get_by_id(data))


@app.route('/create/sasq',methods=['POST'])
def create_sasq():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Sasq.validate_sasq(request.form):
        return redirect('/new/sasq')
    data = {
        "location": request.form["location"],
        "description": request.form["description"],
        "num_of_sasq": int(request.form["num_of_sasq"]),
        "date_siting": request.form["date_siting"],
        "user_id": session["user_id"]
    }
    Sasq.save(data)
    return redirect('/dashboard')

@app.route('/edit/sasq/<int:id>')
def edit_sasq(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_sasq.html",edit=Sasq.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/sasq',methods=['POST'])
def update_sasq():
    
    if 'user_id' not in session:
        return redirect('/logout')
    if not Sasq.validate_sasq(request.form):
        return redirect('/edit/sasq/'+request.form['id'])
    data = {
        "location": request.form["location"],
        "description": request.form["description"],
        "num_of_sasq": int(request.form["num_of_sasq"]),
        "date_siting": request.form["date_siting"],
        "id": request.form['id']
    }
    Sasq.update(data)
    return redirect('/dashboard')

@app.route('/sasq/<int:id>')
def show_sasq(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_sasq.html",sasq=Sasq.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy/sasq/<int:id>')
def destroy_sasq(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Sasq.destroy(data)
    return redirect('/dashboard')