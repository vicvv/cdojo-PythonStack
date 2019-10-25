from flask import Flask,redirect, render_template, request, flash,session
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "blah"

@app.route("/")
def index():  
    myconnect = connectToMySQL("dojo_sur")
    print(myconnect)
    dojos = myconnect.query_db('SELECT * FROM dojos;') 
    print("Alldojos:",dojos)
    if dojos:
        for dojo in dojos:
            print(dojo['name'])
            print(dojo['location'])
            print(dojo['language'])
            print(dojo['message'])
            return render_template("index.html", dojos=dojos)
    else:
        print("I am here because my table is empty")
        return render_template("index.html")
    

@app.route('/add_dojo', methods=['POST'])

def add_dojo():
    print("I am in add_dojo")
    if len(request.form['name']) < 1:
    	flash("Please enter Dojo's name")
    if len(request.form['location']) < 1 or request.form['location'] == "Location":
    	flash("Please select Dojo's location")
    if len(request.form['language']) < 1 or request.form['language'] == "Language":
        flash("Please select the Language")
    if len(request.form['message']) > 120:
        flash("Message should not be more than 120 characters long")
    
    if not '_flashes' in session.keys():
        query = "insert into dojos(name, location, language, message, created_at, updated_at) VALUES (%(dn)s,%(dl)s,%(dlan)s,%(dm)s, now(),now());"
        print(query)

        data = {
            'dn' : request.form['name'],
            'dl' : request.form['location'],
            'dlan' : request.form['language'],
            'dm' : request.form['message'],
        }
        myconnect = connectToMySQL("dojo_sur")
        myconnect.query_db(query,data)

        return redirect ("/")

    return redirect ("/")

if __name__ == '__main__':
    app.run( debug = True)