from django.shortcuts import render, redirect

def index(request):
    return redirect('/home')

def home(request):
    return render(request, "blog/home.html")
    
def about(request):
    return render(request, "blog/about.html")
