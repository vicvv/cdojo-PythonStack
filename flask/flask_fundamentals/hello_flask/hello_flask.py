from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def succerss():
    return "Dojo! yay!!"

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    if name.isalpha():
        return "Hi " + name
    else:
        return("name should be string not " + name)

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and idcopy
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " 

@app.route('/repeat/<num>/<word>') # for a route '/users/____/____', two parameters in the url get passed as username and idcopy
def repete(num, word):
        if word.isalpha()  and  num.isdigit():
            return (str(word + " " ) * int(num))
        else:
            return ("Sorry, no responce, try again!")
   
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
