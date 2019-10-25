from flask import Flask, render_template
app = Flask(__name__)
@app.route('/checkboard')

def index():  
        return render_template("index.html", times = 8, times1 = 8)

@app.route('/checkboard/<num>')        
def index1(num):  
    return render_template("index.html",  times = 8, times1=int(num))

@app.route('/checkboard/<num1>/<num2>')        
def index2(num1,num2):  
    return render_template("index.html",  times = int(num1), times1=int(num2))

@app.route('/checkboard/<num1>/<num2><color1><color2>')        
def index3(num1,num2,color1,color2):  
    return render_template("index.html",  times = int(num1), times1=int(num2), color1 = color1, color2=color2)
    
if __name__=="__main__":
    app.run(debug=True)