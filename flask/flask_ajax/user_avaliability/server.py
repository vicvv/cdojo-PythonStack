from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL

db = 'userid_detection'

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/add', methods=['POST'])
def add_new_user():
    print("I am in newuser")

    mycon = connectToMySQL(db)
    query = "insert into users (username, email) VALUES(%(un)s,%(ue)s);"
    data = {
        'un': request.form['name'],
        'ue': request.form['email']
    }
    mycon.query_db(query,data)
    return redirect ('/')

@app.route("/username", methods=['POST'])
def username():
    print("I am in username")
    found = False
    mysql = connectToMySQL(db)        # connect to the database
    query = "SELECT username from users WHERE username = %(user)s;"
    data = {'user': request.form['name']}
    result = mysql.query_db(query, data)
    if result:
        found = True
    return render_template('partial.html', found=found)  # render a partial and return it
# Notice that we are rendering on a post! Why is it okay to render on a post in this scenario?
# Consider what would happen if the user clicks refresh. Would the form be resubmit


@app.route("/usersearch")
def search():
    mysql = connectToMySQL(db)
    query = "SELECT * FROM users WHERE username LIKE %%(name)s;"
    data = {
        "name" : request.args.get('name') + "%"  # get our data from the query string in the url
    }
    results = mysql.query_db(query, data)
    return render_template("success.html", users = results) # render a template which uses the results

if __name__ == '__main__':
    app.run( debug = True)
