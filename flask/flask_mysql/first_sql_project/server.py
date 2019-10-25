from flask import Flask, request, redirect,render_template, flash, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)

app.secret_key="very secure"

@app.route("/")
def index():
    mysql = connectToMySQL('demo_db')
    print(mysql)
    friends = mysql.query_db('SELECT * FROM friends;')  
    print(friends, type(friends))
    for friend in friends:
        print(friend['first_name'])
    return render_template("index.html", friends = friends)

@app.route("/create_friend", methods=['POST'])
def addfriend():
    if len(request.form['first_name']) < 1:
    	flash("Please enter a first name")
    if len(request.form['last_name']) < 1:
    	flash("Please enter a last name")
    if len(request.form['occupation']) < 2:
    	flash("Occupation should be at least 2 characters")
    
    if not '_flashes' in session.keys():
        query = "INSERT into friends(first_name, last_name, occupation, created_at, updated_at) VALUES(%(fn)s, %(ln)s,%(oc)s, now(), now());"
        data = {
            'fn': request.form['first_name'],
            'ln': request.form['last_name'],
            'oc': request.form['occupation']
        }

        db = connectToMySQL("demo_db")
        db.query_db(query,data)
        return redirect ("/")
    return redirect('/') 
            
if __name__ == "__main__":
    app.run(debug=True)
