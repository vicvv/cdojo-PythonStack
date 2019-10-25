from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("start.html")

@app.route('/result', methods=["POST"])
def process_form():
    print("*"*50)
    print(request.form)
    print(f"username submitted: {request.form['username']}")
    print(f"email submitted: {request.form['email']}")
    print(f"location submitted: {request.form['location']}")
    print(f"language submitted: {request.form['language']}")
    print(f"dogs submitted: {request.form['dogs']}")
    print(f"pet submitted: {request.form['pet']}")
    print(f"coments submitted: {request.form['coment']}")
    return render_template("result.html",
            name=request.form["username"], email=request.form["email"],
            location=request.form["location"],language=request.form["language"],
            dog=request.form["dogs"], pet=request.form["pet"],
            coment=request.form["coment"])


if __name__=="__main__":
    app.run(debug=True)