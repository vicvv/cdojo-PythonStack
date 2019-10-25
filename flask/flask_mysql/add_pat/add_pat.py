from flask import Flask,redirect, render_template, request
from mysqlconnection import connectToMySQL
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():  
    myconnect = connectToMySQL("pets")
    print(myconnect)
    allpets = myconnect.query_db('SELECT * FROM pets;') 
    print("Allpets:",allpets)
    for pet in allpets:
        print(pet['name'])
        print(pet['type'])
        print(pet['color'])
        print(pet['created_at'])
        print(pet['updated_at'])

        return render_template("index.html", allpets=allpets)
    else:
        print("I am here for some reason??")
        return render_template("index.html")
    

@app.route('/add_pet', methods=['POST'])

def add_pet():
    print("I am in add_pet")
    #query = "insert into pets(name, type, color, created_at, updated_at) VALUES (%(pn)s,%(pt)s,%(pc)s, now(), now());"
    query = "insert into pets(name, type, color, created_at, updated_at) VALUES (%(pn)s,%(pt)s,%(pc)s, now(), now());"
    print(query)

    data = {
        'pn' : request.form['name'],
        'pt' : request.form['type'],
        'pc' : request.form['color']

    }
    myconnect = connectToMySQL("pets")
    myconnect.query_db(query,data)

    return redirect ("/")

if __name__ == '__main__':
    app.run( debug = True)

