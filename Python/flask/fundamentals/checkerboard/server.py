from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/board")
def checkerboard():
    return render_template("checkerboard.html",row=8,col=2,color1="red",color2="black") 

@app.route("/board/<int:col>")
def checkerboard_col(col):
    return render_template("checkerboard.html",row=8,col=col,color1="red",color2="black") 

@app.route("/board/<int:col>/<int:row>")
def checkerboard_row(row,col):
    return render_template("checkerboard.html",row=row,col=col,color1="red",color2="black") 

@app.route("/board/<int:col>/<int:row>/<string:color1>/<string:color2>")
def checkerboard_color(row,col,color1,color2):
    return render_template("checkerboard.html",row=row,col=col,color1=color1,color2=color2) 

if __name__=="__main__":
    app.run(debug=True)
