from django.shortcuts import render, redirect
from random import randint
from datetime import datetime
from  . models import User


def index(request):
    context = {
        "allusers" : User.objects.all()
    }
    return render(request,"users_app/index.html", context)