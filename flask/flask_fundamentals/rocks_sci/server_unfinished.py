from flask import Flask, render_template, request, redirect,session
from random import randint
from datetime import datetime


app = Flask(__name__) 
app.secret_key = "sfsdfsdf" 

@app.route('/')         
def index():   
    return render_template("index.html")

# @app.route('/process', methods=['POST'])  

# def process():
#     pass

if __name__ == '__main__':
    app.run( debug = True)