from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
#  
# def index (request):
#     word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
#     response = requests.get(word_site)
#     WORD = response.content.splitlines()[0]     
#     return render(request,'random_word/index.html',WORD)

def index(request):
    print("I am in index")
    return render(request,'random_word/index.html')
    # word = get_random_string(length=14) 
    # context ={
    #    'randomword': word
    # }

    # if 'count' not in request.session:
    #     request.session['count'] = 1
    # print(context)
    # return render(request,'random_word/index.html',context)
    

def generate(request):
    print("I am in generate")
    word = get_random_string(length=14) 
    context = {
       'randomword': word
    }

    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    print(context)
    return render(request,'random_word/index.html',context)
   

def reset(request):
    print("I am in reset")
    try:
        request.session['count'] = 1
    except KeyError:
        pass
    #return redirect('index')
    return render(request,'random_word/index.html')