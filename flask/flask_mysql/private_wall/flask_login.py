from flask import Flask, render_template, request, redirect, flash,session
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt       
# from flask.ext.bcrypt import Bcrypt

#db="flask_ulogin"
db = "private_wall"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    print("I am in register")

    myconn = connectToMySQL(db)
    querry = "select email from users where email =  %(email)s;" 
    data = {
            'email' : request.form['email']
            
        }

    myselect = myconn.query_db(querry, data)
    print("That is what comming form select:",myselect)
    myerr={}

    rulesp =[lambda s: any(x.isupper() for x in s), # must have at least one uppercase
            lambda s: any(x.islower() for x in s),  # must have at least one lowercase
            lambda s: any(x.isdigit() for x in s),  # must have at least one digit
            lambda s: len(s) >= 8                   # must be at least 7 characters
            ]
    
    rulesn =[lambda s: any(x.isalpha() for x in s), # must be letters      
            lambda s: len(s) > 2                  # must be at least 2 characters
            ]

    passstring = "password must have at least one uppercase \nat least one lowercase\n at least one digit\nat least 7 characters"
    
    if not EMAIL_REGEX.match(request.form['email']):  
        flash("Invalid email address!")
        myerr['email'] = "Invalid email address!"
    print(request.form['email'] )

    if myselect and request.form['email'] in myselect[0]['email']:
        print("Email is in db")
        flash(f"{request.form['email']} is already registered")

    if not all(rule(request.form['fname']) for rule in rulesn):
        flash("first name input has issue")
        myerr['fname']= "fix first name"

    if not all(rule(request.form['lname']) for rule in rulesn):
        flash("last name input has issues")
        myerr['lname'] = "last name input has issue"

    
    if not all(rule(request.form['password']) for rule in rulesp):
        flash(passstring)
    if request.form['password'] != request.form['vpassword']:
        myerr['vpassw'] = "Password does not match!"
        flash("Password does not match!")
   

    if not '_flashes' in session.keys():	# no flash messages means all validations passed
        # add user to database
        print("flash is empty!")
        pw_hash = bcrypt.generate_password_hash(request.form['password'])  
        print(pw_hash) 
        myconn = connectToMySQL(db)
        querry = "insert into users(username, fname,lname, email, password) VALUES(%(username)s,%(fname)s,%(lname)s, %(email)s, %(password)s);"
        print("query", querry)
        print(request.form)
        data = {
            'username' : request.form['username'],
            'fname' : request.form['fname'],
            'lname' : request.form['lname'],
            'email' : request.form['email'],
            'password': pw_hash 
        }

        myinsert = myconn.query_db(querry,data)

        if (myinsert):
             flash("You successfully registered!")

        return redirect ('/')
    else:
        return render_template('index.html', color = "text-danger",myerr=myerr)
    

@app.route('/login', methods=['POST'])
def login():
    print("I am in login")
    mysql = connectToMySQL(db)
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = { "email" : request.form["email"] }
    result = mysql.query_db(query, data)
    if len(result) > 0:
        # assuming we only have one user with this username, the user would be first in the list we get back
        # of course, we should have some logic to prevent duplicates of usernames when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            # if we get True after checking the password, we may put the user id in session
            session['user_id'] = result[0]['id']
            session['fname'] = result[0]['fname']
            # never render on a post, always redirect!
            return redirect('/success')
    # if we didn't find anything in the database by searching by username or if the passwords don't match,
    # flash an error message and redirect back to a safe route
    flash("You could not be logged in")
    return redirect("/")

@app.route('/success')
def success():
    if 'user_id' in session:
        print("am i in addform??")
        mysql = connectToMySQL(db)
        query = "SELECT id, fname FROM users;"
        users = mysql.query_db(query)

        mysqlm = connectToMySQL(db)
        query= "SELECT umessages.id, umessages.message, fname FROM umessages JOIN users on umessages.sender_id = users.id where umessages.reseiver_id = %(reseiver_id)s;"
        #query = "SELECT id, message from umessages where reseiver_id = %(reseiver_id)s;"

        print()
        data = {'reseiver_id': session['user_id']}

        messages = mysqlm.query_db(query,data)
        return render_template('success.html', users=users, messages=messages)
    else:
        return redirect ("/")

@app.route('/logout')
def logout():
    session.clear()  
    return redirect('/')


@app.route('/addmessage', methods=['POST'])
def addmessage():
    print("I am in add message")
    myconn = connectToMySQL(db)
    querry = "insert into umessages(reseiver_id, sender_id, message) VALUES(%(res)s,%(sen)s,%(message)s);"
    print(querry)
    print(request.form)
    data = {   
        'res': request.form['id'],
        'sen' : session['user_id'] ,
        'message' : request.form['message']
    }
    myinsert = myconn.query_db(querry,data)
    print("what is in myisert", myinsert)   
    return redirect ('/success')


@app.route('/success/<int:id>/destroy', methods=['POST'])
def delete_message(id):
    print("I am in delete?", id)
    print(type(id))
    mycon = connectToMySQL(db)
    mquery = "delete from umessages where id=%(id)s and reseiver_id = %(reseiver_id)s;"
    print (mquery)
    data = {
        'id': id,
        'reseiver_id': session['user_id']
        }

    result = mycon.query_db(mquery,data)
    print("result",result)
    if result != None:
        return redirect ('/danger')
    return redirect ('/success')

# @app.errorhandler(404)
# def danger(error):
#      return redirect('/danger')
# @app.errorhandler(405)
# def danger1(error):
#      return redirect('/danger')
@app.route('/danger')
def bad():
    return render_template("danger.html")

if __name__ == '__main__':
    app.run( debug = True)