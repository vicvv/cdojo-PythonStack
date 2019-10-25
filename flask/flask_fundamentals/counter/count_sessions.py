from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template("index.html",count= session['count'])

@app.route('/countsessions' ,methods=['POST'])

def add2():
    print(request.form)
    if request.method== 'POST':
        if request.form.get('AddTwo') == 'AddTwo':
            session['count']+=1
            return redirect ('/')
        if request.form.get("reset") == 'reset':
            session['count']=0
            return redirect('/')
        if request.form.get("increment") is not None:
            value = request.form['increment']
            session['count']+= int(value)
            return redirect('/')

@app.route('/destroy')
def destroy_session():
    session.clear()
    #mykey=session.pop()
    #print("My mysterious session key:" ,mykey)
    return redirect('/')

app.run(debug=True)