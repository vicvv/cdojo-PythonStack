from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from . models import *
from time import strftime

def index(request):
    return redirect("/shows")

def shows(request):
    shows = Show.objects.all()
    context = {"shows": shows}       
    return render(request,"show_app/index.html", context)

def new_show(request):
    return render(request,"show_app/new.html")

def add_new_show(request):
    print("I am in new show form")
    print (request.POST.get('title'))
    print (request.POST.get('network'))
    print (request.POST.get('rday'))
    print (request.POST.get('descr'))


    if len(request.POST["title"]) > 1 and len(request.POST["descr"]) > 5:
        Show.objects.create(
            title=request.POST["title"], \
            network= request.POST["network"],\
            rday = request.POST["rday"],\
            descr = request.POST["descr"]
            )
        messages.add_message(request, messages.INFO, "New Show is added to  db!")
    else:
        messages.add_message(request, messages.INFO, "Cant add show. Something wrong with title or description")
    return redirect("/shows")

def view_show(request, show_id):
    show = Show.objects.get(id = show_id)

    context = {"show":show}
    return render(request, "show_app/show.html", context)

def edit_show(request, show_id):
    show = Show.objects.get(id = show_id)

    context = {"show":show}
    return render(request, "show_app/edit.html", context)

def process_edit(request,show_id):
    show = Show.objects.get(id = show_id)
    print(show.id)
    Show.objects.filter(pk=show_id).update(title=request.POST["title"])
    Show.objects.filter(pk=show_id).update(network=request.POST["network"])
    #Show.objects.filter(pk=show_id).update(rday='request.POST["rday"]')
    Show.objects.filter(pk=show_id).update(descr=request.POST["descr"])
    return redirect ("/shows")

def remove_show(request, show_id):
    Show.objects.filter(id=show_id).delete()
    return redirect ("/shows")
