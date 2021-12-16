from flask import Flask,render_template,redirect,request, session
from flask_app import app
from flask_app.models.user import User
from flask import session
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
# which is made by invoking the function Bcrypt with our app as an argument
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/register', methods=['POST'])
def register():
    # validate the form here ...
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    User.save(data)

    return redirect("/dashboard")


@app.route('/')
def index():
    return redirect('/users')



@app.route('/users')
def users():
    return render_template("index.html")


@app.route('/users/create',methods=['POST'])
def create():
    print(request.form)
    if not User.validate_data(request.form):
        return redirect('/')
    data ={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'user.id' not in session:
        return redirect('/logout')
    # data={
    #     id:session['user.id']
    # }
    # return render_template('dashboard.html',user=User.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')