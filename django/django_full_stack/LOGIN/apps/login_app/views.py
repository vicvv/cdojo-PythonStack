from django.shortcuts import render, redirect
from django.contrib import messages
#from .forms import UserRegisterForm
from . models import *
from django.contrib.auth.decorators import login_required
import bcrypt


def index(request):
    return redirect ("/logmein")

def logmein(request):
    return render (request, "login_app/login_register.html")

def register(request):
    print(request.POST['username'])
    print(request.POST['first_name'])
    print(request.POST['last_name'])
    print(request.POST['email'])
    print(request.POST['password'])
    print(request.POST['password2'])

    request.session['username'] = request.POST.get('username')
    request.session['first_name'] = request.POST.get('first_name')
    request.session['last_name'] = request.POST.get('last_name')
    request.session['email'] = request.POST.get('email')
    print("whats in session:", request.session['username'])

    errors = MyLogin.objects.basic_validator(request.POST)
    print(errors, request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            print(key, value)
            messages.error(request, key ,value)
            messages.add_message(request, messages.INFO, "Cant register the user, try again!")
            return redirect('/logmein')
    
    password=request.POST['password']
    mypassstring = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    print(mypassstring)

    try:
        checkemail = MyLogin.objects.get(email = request.POST['email'])
        if request.POST['email'] == checkemail.email:
            messages.add_message(request, messages.INFO, "YOU ARE ALREADY REGISTERED!")
            return redirect('/logmein')
    except MyLogin.DoesNotExist:       
        MyLogin.objects.create(
            username=request.POST['username'],\
            first_name=request.POST['first_name'],\
            last_name=request.POST['last_name'], \
            email=request.POST['email'],\
            password = mypassstring, 
            )
        messages.add_message(request, messages.INFO, "You have successfully registered!")
        return redirect ("/logmein")

def login(request):
    
    print("I am in login!")
    # checking if password or email fields are empty
    if not request.POST['email'] or not request.POST['password']:
        return redirect ("/logmein")

    print(request.POST['email'])
    print(request.POST['password'])

    password=request.POST['password']
    getinfo = MyLogin.objects.get(email = request.POST['email'])
    
    request.session['id'] = getinfo.id
    print(getinfo.email, getinfo.password)

    val = bcrypt.checkpw(password.encode('utf8'), getinfo.password.encode('utf8'))
    print(val)

    if val:
            request.session['first_name'] = getinfo.first_name
            return redirect ('/logmein/success')

    messages.add_message(request, messages.INFO, "Email or password does not match!")
    return redirect ("/logmein")

def success(request):
    if  'id' in request.session:
        return render (request, "login_app/success.html")
    return redirect ("/logmein")

def logout(request):
    request.session.clear() 
    return redirect ("/logmein")

