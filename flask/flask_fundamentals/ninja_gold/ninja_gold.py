from flask import Flask, render_template, request, redirect,session
from random import randint
from datetime import datetime


app = Flask(__name__) 
app.secret_key = "sfsdfsdf" 

@app.route('/')         
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['gameresult'] =[]
    return render_template("index.html")




@app.route('/process', methods=['POST'])  
def process():
    print("I am in porcess")
    
    if request.form.get("reset") == 'reset':
        print("I am in reset")
        session['gold'] = 0
        session['gameresult'] =[]
        return redirect('/')

    building = request.form['building']
    gold = process_request(building)

    #print("what is in session??", session['gold'], type(session['gold']))
    (disable,invisible, message, tcolor) = check_session(session['gold'])
    print (disable, invisible, message, tcolor)
    #return redirect ('/')
    return render_template("index.html",disable = disable,invisible = invisible, message=message, tcolor=tcolor)


def process_request(building):
    print("I am in porcerss_request")

    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    data = {
        'farm': randint(10,21),
        'cave': randint(5,11),
        'house': randint(2,11),
        'casino': randint(-50, 51),     
    }

    if building in data:
        gold = data[building]
        session['gold'] += gold
        return gold


    if gold < 0:
        print("you lost")
        color = "text-danger"
        result = f"Sorry you lost {gold} in {building} on {date_time}"
        #print("This is result",result)
        session['gameresult'].insert(0,{"result":result, "color":color})
              
    else:
        print("you won")
        color = "text-success"
        result = f"You won {gold} in {building} on {date_time}! Congradulation!"
        print("This is result",result)
        session['gameresult'].insert(0,{"result":result, "color":color})


def check_session(ses_total):
    print("in check session")
    print(type(ses_total))
    print(ses_total)

    if ses_total >= 500:
        print("in > 500")
        (disable,invisible,message,tcolor) = ("","visible","You Won!","text-success")
        print( disable,invisible, message, tcolor)
        return( disable,invisible, message, tcolor)
    elif ses_total < -1:
        print("in < -1")
        (disable,invisible,message,tcolor) = ("","visible","You lost!","text-danger")        
        print( disable,invisible, message, tcolor)
        return( disable,invisible, message, tcolor)
    else:
        print("nothing to do here ... returnting")
        (disable,invisible,message,tcolor) = ("disabled","invisible"," ","text-danger")
        return( disable,invisible, message, tcolor)



if __name__ == '__main__':
    app.run( debug = True)

