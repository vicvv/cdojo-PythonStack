from flask import Flask, render_template
app = Flask(__name__)

@app.route('/tables')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    #return render_template("index_tables.html", random_numbers = [3,1,5], users = users)
    return render_template("index_tables.html", users = users)

if __name__=="__main__":
    app.run(debug=True)