from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session

app = Flask(__name__)
app.secret_key ='root'


@app.route('/')
def clickadd():
    if 'clickadd' in session:
        session['clickadd'] = session.get('clickadd') + 1
    else:
        session['clickadd'] = 0
    return render_template('index.html')

@app.route('/addtwo')
def clickaddtwo():
    if 'clickadd' in session:
        session['clickadd'] = session.get('clickadd') + 1
    else:
        session['clickadd'] = 0
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)