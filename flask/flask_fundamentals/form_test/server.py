from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process_form():
    print("*"*50)
    print(request.form)
    print(f"username submitted: {request.form['username']}")
    print(f"email submitted: {request.form['email']}")
    session['username'] = request.form['username']
    session['email'] = request.form['email']
    return redirect("/show")

@app.route("/show")
def show_request():
    return render_template("info.html",
    name=session["username"], 
    email=session["email"]
    )


if __name__=="__main__":
    app.run(debug=True)