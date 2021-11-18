from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:num>')
def test(num):
    return render_template('test.html',num = num)

@app.route('/<int:num>/<string:color>')
def test_color(num,color):
    return render_template('test.html',num = num, color = 'color')

if __name__=="__main__":
    app.run(debug=True)

    
