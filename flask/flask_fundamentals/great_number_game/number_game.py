from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 


@app.route('/')
def index():
    print("I am Here")
    session['randnum'] = random.randint(1,100)
    print("Rundom number is:", session['randnum'])
    return render_template("index.html")

@app.route('/guess',  methods=['POST'])
def guessed():
    
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    lost = "Sorry you lost! The number was " + str(session['randnum'])+ " Starting new game!"
    print("I am in guessed")
    print(request.form['numberin'])

    if request.form.get("reset") == 'reset':
        return render_template("index.html")
        
    if int(request.form['numberin'] )== int(session['randnum']):
        print("you win!")
        winmessage = "We have a winner!!! Want to try again?"
        return render_template("result.html", message=winmessage)

    elif int(request.form['numberin'] ) > int(session['randnum']):
        toobig = "Too big! try smaller number"
        print("count",session['count'])
        result= checkcount(session['count'])
        if result == False:
            
            return render_template("index.html", lost=lost)
        return render_template("result.html", message=toobig)

    elif int(request.form['numberin'] ) < int(session['randnum']):
        toosmal = "Too small! try bigger number"    
        print("count",session['count'])
        result = checkcount(session['count'])
        if result == False:
           
            return render_template("index.html", lost=lost)
        return render_template("result.html", message=toosmal)
        
def checkcount(count):
    print(count)
    if count > 3:
        session['count'] = 0
        print("you lost")
        return False
    else:
        return True

app.run(debug=True)