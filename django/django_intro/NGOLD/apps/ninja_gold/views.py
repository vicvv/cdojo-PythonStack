from django.shortcuts import render, redirect
from random import randint
from datetime import datetime
#from . myforms import *


def index(request):   
    if 'count' not in request.session:
        request.session['count'] = 0
    if not request.session.get('activity', None):
        request.session.setdefault('activity', [ ])

    # context = {
    # 'farmForm': farmForm(),
    # 'houseForm': houseForm(),
    # 'casinoForm': casinoForm(),
    # 'caveForm': caveForm(),
    # }

    # return render(request,"ninja_gold/index.html", context)
    return render(request,"ninja_gold/index.html")


def process_money(request):

    print("I am in proces money")
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    #print(date_time)

    data = {
        'farm':randint(10,21),
        'cave':randint(5,11),
        'house': randint(2,11),
        'casino': randint(-50, 51),     
    }
    
    if request.POST.get("building", False) in data:
        buiding = request.POST.get("building", False)

        print(buiding,data[buiding])
        request.session['count'] += data[buiding]

        if data[buiding] > 0:
            color= {'color':'text-success'}   
            myvar = f"You won {data[buiding]} in {buiding} on {date_time}"
            request.session['activity'].insert(0,(myvar))
        else:
            color = {'color':'text-danger'}
            myvar = f"Lost {data[buiding]} in {buiding} on {date_time}"
            request.session['activity'].insert(0,(myvar) )

    return render(request,"ninja_gold/index.html", color)
   