from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import User

from flask_bcrypt import Bcrypt # pipenv install flask pymysql flask-bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def lr():
    return render_template('lr.html')

@app.route('/register', methods=["POST"])
def register():
    # Validation process here...
    encrypted_pw = "" # Bcrypt encryption here...
    data = {
        "name": request.form['user_name'],
        "email": request.form['email'],
        "password": encrypted_pw,
    }
    user_id = User.create_one(data) # INSERT queries give back an id
    # IMPORTANT step here...
    return redirect('/dashboard')

@app.route('/login', methods=["POST"])
def login():
    data = {"email": request.form['email']} # Step 1: Check if email exists in database
    user_with_email = User.get_by_email(data) # Returns False if email is NOT found in database
    if user_with_email == False:
        flash("Invalid Email/Password") # Why not "Wrong email?"
        return redirect('/')
    if not bcrypt.check_password_hash(user_with_email.password, request.form['password']): # Step 2: Check if password from form matches password for user_with_email
        flash("Invalid Email/Password") # Why not "Wrong password?"
        return redirect('/')
    # IMPORTANT step here...
    return redirect('/dashboard') # If we got to here, it means the login was a success, you have the option to flash a success message

@app.route('/dashboard')
def main_page():
    # IMPORTANT step here now that we are in the application...
    data = {
        "id": "" # Something important here...
    }
    one_user = User.get_one(data)
    return render_template('main_page.html', current_user = one_user)

# Logout method here...