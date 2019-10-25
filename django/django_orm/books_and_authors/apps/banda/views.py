from django.shortcuts import render, redirect, reverse
from . models import Author
from . models import Book
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR

# def index(request):
#     return render(request, "banda/index.html")


def index(request):    
    return render(request,"banda/index.html")

def books(request):
    context = {
        'allbooks': Book.objects.all()
    }
    return render(request,"banda/books.html",context)

#i nsert book into database
def new_book(request):
    print("I am in add_book")
    print(request.POST["title"])
    print(request.POST["description"])

    if len(request.POST["title"]) > 1 and len(request.POST["description"]) > 5:
        Book.objects.create(title=request.POST["title"], description=request.POST["description"])
        messages.add_message(request, messages.INFO, "New Book is added to db!")
    else:
        messages.add_message(request, messages.INFO, "Cant add book. Something wrong with title or description")
    
    return redirect("/banda/books")

# view single book
def show_book(request, number):
    book = Book.objects.get(id=int(number))
    book_authors = book.authors.all()
    all_authors = Author.objects.all()
    context = {
        "book": book,
        "book_authors": book_authors,
        "all_authors": all_authors
    }
    print(context)
    return render(request, "banda/showbook.html", context)

# add author to the book
def add_author(request,number):
    #this_book.author.add(Author.objects.get(id=int(number)))
    book_id = int(number)
    author_id = int(request.POST["author"])
    
    onebook = Book.objects.get(id=book_id)
    oneauthor= Author.objects.get(id = author_id)
    onebook.authors.add(oneauthor)
    
    messages.add_message(request, messages.INFO, "Author added!")    
    return redirect(f"/banda/books/{number}")


def authors(request):

    context = {
        'allauthors': Author.objects.all()
        }
    return render(request, "banda/authors.html", context)

def new_author(request):
    print("I am in new author form")
    if request.method == 'POST':
        print (request.POST.get('first_name'))
        print (request.POST.get('last_name'))
        print (request.POST.get('notes'))
        #return redirect("/banda/authors")


    if len(request.POST["first_name"]) > 2 and len(request.POST["last_name"]) > 2:
        Author.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"],notes=request.POST["notes"])
        messages.add_message(request, messages.INFO, "New Author is added to db!")
    else:
        messages.add_message(request, messages.INFO, "Cant chreate and Author. Something wrong with first/last name or notes")
    
    return redirect("/banda/authors")

def show_author(request, number):
    author = Author.objects.get(id=int(number))
    author_book = author.books.all()
    all_books = Book.objects.all()
    context = {
        "author": author,
        "author_book": author_book,
        "all_books": all_books
    }
    print(context)
    return render(request, "banda/showauthor.html", context)

def add_book(request,number):
    #this_book.author.add(Author.objects.get(id=int(number)))
    author_id = int(number)
    book_id = int(request.POST["book"])
    
    oneauthor = Author.objects.get(id=author_id)
    onebook= Book.objects.get(id = book_id)
    oneauthor.books.add(onebook)   
    messages.add_message(request, messages.INFO, "Book added!")
    
    return redirect(f"/banda/authors/{number}")



