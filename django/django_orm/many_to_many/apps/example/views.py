from django.shortcuts import render,redirect
from . models import Author
from . models import Book
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR

def index(request):
    return render(request, "example/index.html")


def books(request):
    context = {
        'allbooks': Book.objects.all()
    }

    return render(request,"example/books.html",context)

def authors(request):

    context = {
        'allauthors': Author.objects.all()
        }

    return render(request, "example/authors.html", context)

def add_author(request):
    print("I am here")
    if request.method == 'POST':
        print (request.POST.get('first_name'))
        print (request.PPST.get('last_name'))
        print (request.PPST.get('notes'))

        return render(request, "example/authors.html")


