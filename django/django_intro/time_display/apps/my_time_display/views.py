from django.shortcuts import render
from time import gmtime, strftime
from django.template import Template
    
def index(request):
    context = {"time": strftime("%b %d %Y %I:%M%p", gmtime())}
   
    print(context['time'])
    return render(request,'my_time_display/index.html', context)

