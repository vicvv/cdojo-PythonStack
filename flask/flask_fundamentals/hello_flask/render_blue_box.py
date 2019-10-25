from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play/<num>/<color>')

def index(num,color):  
        return render_template("box_index.html", phrase="hello", color=color,times =int(num))
    	# notice the 2 new named arguments!
if __name__=="__main__":
    app.run(debug=True)
