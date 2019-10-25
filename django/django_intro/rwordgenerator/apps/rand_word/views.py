from django.shortcuts import render,redirect
from django.template import Template
from django.utils.crypto import get_random_string


def index(request):
    print("I am in index")
    return render(request,'rand_word/index.html')

def generate(request):
    print("I am in generate")
    myword = get_random_string(length=14)
    context = {
        'word': myword,
    }
    print(context)

    if 'count' not in request.session:
        request.session['count'] = 1 
    else:
        request.session['count']+=1
    return render (request,'rand_word/index.html',context)

def reset(request):
    try:
        request.session['count'] = 1
    except Exception as e:
        print(e)
    return render(request, 'rand_word/index.html')




    

