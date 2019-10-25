from flask import Flask,redirect, render_template, request, redirect,session, flash
from mysqlconnection import connectToMySQL
from datetime import datetime
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
app = Flask(__name__)
app.secret_key="hahhah"
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/addemail' ,methods =['POST'])

def addemail():
    # email = request.form['email']
    # mycon1 = connectToMySQL('emailvld')
    # query = "select email from emails where email = ? " , str(email)
    # myqres1 = mycon1.query_db(query)
    # print(myqres1)

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address!")
        return redirect ('/invalid/Invalid email format')
   
    # elif emcheckresult == True:
    #     return redirect ('/invalid/Email already exists!')
    else:

        print ("I am in /addemail", request.form['email'])
        mycon = connectToMySQL('emailvld')
        query = "insert into emails (email, created_at, updated_at) VALUES (%(em)s, now(), now());"
        print(query)
        data = {
            'em' : request.form['email']
        }
        myqres = mycon.query_db(query, data)
        if (myqres == False):
            return redirect ('/invalid/Email already exists!')
        else:
            print("Result from db query: ", myqres)       
            return redirect ('/result/Thank you for providing correct email!')

@app.route('/result/<message>')
def result(message):
    mycon = connectToMySQL('emailvld')
    query = "select * from emails;"   
    myqres = mycon.query_db(query)
    return render_template ("result.html", myqres=myqres, message=message)

@app.route('/invalid/<msg>')
def invald(msg):
    return render_template('invalid.html',msg=msg)

@app.route('/result/<int:id>/destroy')
def destoy(id):
    mycon = connectToMySQL('emailvld')
    query = "delete from emails where id = "  + str(id) 
    mycon.query_db(query)

    mycon = connectToMySQL('emailvld')
    query = "select * from emails;"   
    myqres = mycon.query_db(query)
    message="Email was deleted... maybe..."
    return render_template ("result.html", myqres=myqres, message=message)
    


if __name__ == '__main__':
    app.run( debug = True)