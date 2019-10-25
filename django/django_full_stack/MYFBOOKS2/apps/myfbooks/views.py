from django.shortcuts import render
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from . models import *

def index(request):
    return redirect ('/home')

def about(request):
    liked_books = Book.objects.all().filter(likes__id__contains=request.session['id'])

    context = {
        'myfavbooks':liked_books
    }
    return render(request,"myfbooks/about.html", context)
    

def home(request):
    if  'id' in request.session:   
        #user = MyUser.objects.filter(id=request.session['id'])
        liked_books = Book.objects.all().filter(likes__id__contains=request.session['id'])
        disliked_books = Book.objects.all().exclude(likes__id__contains=request.session['id'])
    
        context ={
            'liked_books': liked_books,
            'disliked_books': disliked_books,
            }
        return render (request, "myfbooks/home.html", context)
    return redirect ("/logmein/login")

def newbook(request):
    if  'id' in request.session:
        return render(request,"myfbooks/newbook.html")
    return redirect ("/logmein/login")

def newbookform(request):

    print("user:", request.session['id'])
    try:
        print("title:", request.POST['title'])
        print("description:", request.POST['description'])
    except Exception as e:
        print(e)
   
    errors = Book.objects.input_validator(request.POST)
    print(errors, request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            # print(key, value)
            #messages.error(request, key + value)
            messages.add_message(request, messages.INFO, value)
        return redirect ('/newbook')

# >>> user = MyUser.objects.get(id=1)
    my_book = Book.objects.create(
        title=request.POST['title'],\
        description=request.POST['description'], \
        uploaded_by_id = request.session['id'])
    if my_book:
        messages.add_message(request, messages.INFO, "You have successfully added a new book!")
        return redirect ('/home')
    else:
        messages.add_message(request, messages.INFO, "Cant add the book this time")

def likebook(request,book_id):
    print("I am in like")
    # >>> my_book = Book.objects.create(title="First Book", description="About Birds", uploaded_by = user)
    # >>> my_book = Book.objects.create(title="Second Book", description="About Sage", uploaded_by = user)
    # >>> this_book = Book.objects.get(id=1)
    # >>> this_user = MyUser.objects.get(id = 2)
    # >>> this_book.likes.add(this_user)

    this_book = Book.objects.get(id=book_id)
    this_user = MyUser.objects.get(id = request.session['id']) #get it from session
    this_book.likes.add(this_user)
    #print("this book's likes",this_book.likes.all().values())
    wholikedit = this_book.likes.filter(id = request.session['id'])
    print(wholikedit.values())
    print("who liked it?",wholikedit.values()[0]['id'])

    return redirect ('/home')
#----------------------------------------------------------------------------

def unlikebook(request, book_id):
    print("I am in unlike")
    this_book = Book.objects.get(id=book_id)
    this_user = MyUser.objects.get(id = request.session['id']) #get it from session
    this_book.likes.remove(this_user)
    return redirect ('/home') 

def viewbook(request,book_id):

    book = Book.objects.get(id = book_id)
    liked_by = book.likes.all()

    context = {
        "book": book,
        "liked_by": liked_by,
        "view":'1',
    } 

    return render (request, "myfbooks/viewedit.html", context)

def editbook(request, book_id):
    book = Book.objects.get(id = book_id)
    liked_by = book.likes.all()
    context = {

        "book" : book,
        "liked_by" : liked_by
    }
    return render (request, "myfbooks/viewedit.html", context)

def process_edit(request,book_id):
    print("I am in edit")

    book = Book.objects.get(id=book_id)
   

    errors = Book.objects.basic_validator(request.POST)
    print(errors, request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            print(key, value)
            messages.error(request, key ,value)
            messages.add_message(request, messages.INFO, key + ' ' + value)
        return redirect('/home/'+ book_id + '/edit')
    #uploaded_by_id = MyUser.objects.get(id=request.session['id'])
    #print( "What is in uploaded? ",uploaded_by_id )
    #print(MyUser.objects.get(id=request.session['id']))
    #book.uploaded_by = uploaded_by_id
    book.title = request.POST['title'] 
    book.description = request.POST['description']
    book.save()

    # book.update(title = request.POST['title'])
    # book.update(description = request.POST['description'])
    messages.add_message(request, messages.INFO, "The book edit was successful")
    return  redirect ('/home')

    
def deletebook(request, book_id):
    Book.objects.filter(id=book_id).delete()
    return  redirect ('/home')