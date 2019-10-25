from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages

from . models import *


def index(request):    
    return redirect ('/home')

def about(request):
    return render (request, 'exam_app/about.html')

def home(request):
    if 'id' in request.session:

        # posts = Message.objects.all()
        # comments = Coment.objects.all()

        # for post in posts:
        #     print(post.id, post.messagetext, post.created_by.first_name, post.created_by.last_name)

        # for comment in comments:
        #     print(comment.id, comment.commenttext,\
        #         comment.tomessage_id, comment.creator.first_name, \
        #             comment.creator.last_name, comment.creator.id)

        # context = {
        #     'posts' : posts,
        #     'comments' : comments
        # }

        # return render (request, 'exam_app/home.html',  context)

        return render (request, 'exam_app/home.html')
    else:
        messages.add_message(request, messages.ERROR, "You have to log in first.")
        return redirect ("/logmein")



# def index(request):
#     #if user tries to view page but has not logged in and created a request.session['id'] redirect to login and registration page with error message
#     if 'id' not in request.session:
#         messages.add_message(request, messages.ERROR, "You have to log in first.")
#         return redirect('/')
#     context = {
#         #trips is set to the data stored in the Trip table where the logged in user is either the creator or a participant
#         'trips': Trip.objects.filter(Q(creator=request.session['id']) | Q(participants=request.session['id'])).distinct() ,
#         #other_trips is set to the data stored in the Trip table where the logged in user is not the creator or a participant
#         'other_trips': Trip.objects.exclude(Q(creator=request.session['id']) | Q(participants=request.session['id'])).distinct()
#     }
#     return render(request, 'app2/app2_index.html', context)
# def add(request):
#     #if user tries to view page but has not logged in and created a request.session['id'] redirect to login and registration page with error message
#     if 'id' not in request.session:
#         messages.add_message(request, messages.ERROR, "You have to log in first.")
#         return redirect('/')
#     return render(request, 'app2/add.html')
# def add_trip(request):
#     #if there are errors add errors to messages and redirect to the 'add a trip' page
#     errors = Trip.objects.trip_validation(request.POST)
#     if len(errors) > 0:
#         for tag, error in errors.iteritems():
#             messages.error(request, error, extra_tags=tag)
#         return redirect('/travels/add')
#     #if there are no errors then create an object in the Trip table with the entered information and link creator to the logged in user
#     else:
#         Trip.objects.create(destination=request.POST['destination'], description=request.POST['description'], start_date=request.POST['travel_from'], end_date=request.POST['travel_to'], creator=User.objects.get(id=request.session['id']))
#         return redirect('/travels')
# def view_trip(request, number):
#     #if user tries to view page but has not logged in and created a request.session['id'] redirect to login and registration page with error message
#     if 'id' not in request.session:
#         messages.add_message(request, messages.ERROR, "You have to log in first.")
#         return redirect('/')
#     #get the information for the trip where the id is the id of the trip that was clicked
#     context = {
#         'trip': Trip.objects.get(id=number)
#     }
#     return render(request, 'app2/view.html', context)
# def join_trip(request, number):
#     #if a user wants to join a trip add them as a participant of the trip
#     Trip.objects.get(id=number).participants.add(request.session['id'])
#     return redirect('/travels')