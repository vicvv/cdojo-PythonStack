from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect

from . models import *


def index(request):    
    return redirect ('/home')

def about(request):
    return render (request, 'wall_app/about.html')

def home(request):
    if 'id' in request.session:

        posts = Message.objects.all()
        comments = Coment.objects.all()

        # for post in posts:
        #     print(post.id, post.messagetext, post.created_by.first_name, post.created_by.last_name)

        # for comment in comments:
        #     print(comment.id, comment.commenttext,\
        #         comment.tomessage_id, comment.creator.first_name, \
        #             comment.creator.last_name, comment.creator.id)

        context = {
            'posts' : posts,
            'comments' : comments
        }

        return render (request, 'wall_app/home.html',  context)
    else:
        return redirect ("/logmein")

def newpost(request):
    print('I am in newpost')
    
    return render (request, 'wall_app/newpost.html')

def newpostform(request):
    print("I am in newpostform")
    print("message:", request.POST['messagetext'])


    print("usr",request.session['id'])
    Message.objects.create(messagetext=request.POST['messagetext'],\
        created_by_id = request.session['id'])
    return redirect ('/home')


def editpost(request,post_id):
    post = Message.objects.get(id=post_id)
    context={
        "post": post,
        "id": post_id
        }
    return render (request, 'wall_app/editpost.html',context)


def editpostform(request,post_id): 
    print("I am in edit form", post_id)
    post = Message.objects.get(id = post_id) 
    print(post, request.POST['messagetext']) 
    post.messagetext = request.POST['messagetext']
    post.save() 
    return redirect ('/home')


def deletemessage(request, post_id):
    print("I am in delete message" ,post_id)
    Message.objects.filter(id=post_id).delete()



def newcoment(request):
    return render (request, 'wall_app/newcoment.html')

def newcomentform(request):
    print("I am in newcommentform")
    print("message:", request.POST['commenttext'])
    print("message_id:", request.POST['postid'])

    Coment.objects.create(commenttext=request.POST['commenttext'],\
        creator_id = request.session['id'],tomessage_id = request.POST['postid'])
    return redirect ('/home')

