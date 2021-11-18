from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
# Ensure this file is being run directly and not from a different module    
# Run the app in debug mode.

@app.route('/dojo')
def dojo():
    return 'Dojo!'

    
@app.route('/say/<word>')
def say(word):
    print(word)
    return "Hi" + word

@app.route('/repeat/<int:num>/<string:repeatword>')
def repeatword(num,repeatword):
    return num*repeatword
    

if __name__=="__main__":
    app.run(debug=True)