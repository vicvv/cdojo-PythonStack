from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/users')
def index():
    mycon = connectToMySQL("users_rest")
    query = "select * from users"
    myusers = mycon.query_db(query)
    return render_template("index.html", myusers = myusers)
   
@app.route('/users/new')
def add_user_view():
	return render_template('new_user.html')

  
@app.route('/add', methods=['POST'])
def add_new_user():
    print("I am in newuser")
    mycon = connectToMySQL("users_rest")

    print(mycon)

    query = "insert into users (name, email, created_at, updated_at) VALUES(%(un)s,%(ue)s,now(), now());"
    print(query)
    data = {
        'un': request.form['name'],
        'ue': request.form['email']
    }
    mycon.query_db(query,data)
    return redirect ('/users')

@app.route('/users/<int:id>/edit')
def add_user_edit(id):
    print(type(id))
    mycon = connectToMySQL("users_rest")
    mquery = "select * from users where id = %(id)s;"
    data = {'id': id}
    print (mquery)
    row = mycon.query_db(mquery, data)
    if row:
        return render_template('edit.html', row=row)
    else:
        return 'Error loading #{id}'.format(id=id)   

@app.route('/update', methods=['POST'])
def update_user():
    print("I am in update user")
    mycon = connectToMySQL("users_rest")
    print(mycon)
    #query = "insert into users (name, email, created_at, updated_at) VALUES(%(un)s,%(ue)s,now(), now());"
    query = "UPDATE users SET name = %(un)s, email=%(ue)s, updated_at = now() WHERE  id=%(id)s"

    print(query)
    data = {
        'id': request.form['id'],
        'un': request.form['name'],
        'ue': request.form['email']
    }

    mycon.query_db(query,data)
    return redirect ('/users')


@app.route('/users/<id>')
def add_user_show(id):
    print("I am in show?")
    print(type(id))
    mycon = connectToMySQL("users_rest")
    mquery = "select * from users where id=%(id)s;"
    print (mquery)
    data = {'id': id}
    row = mycon.query_db(mquery, data)[0]

    print("******* ROW: ", row['id'])
    if row:
        return render_template('show.html', row=row)
    else:
        return 'Error loading #{id}'.format(id=id) 


@app.route('/users/<int:id>/destroy')
def add_user_delete(id):
    print("I am in destroy", id)
    print(type(id))
    mycon = connectToMySQL("users_rest")
    mquery = "delete from users where id=%(id)s;"
    print (mquery)
    data = {'id': id}
    print (mquery)
    row = mycon.query_db(mquery,data)
    print(row)
    return redirect ('/users')

#########################################

if __name__ == '__main__':
    app.run( debug = True)
