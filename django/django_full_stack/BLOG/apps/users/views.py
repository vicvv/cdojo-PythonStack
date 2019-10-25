from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegisterForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created succesfully!')
            #return redirect('login')
            return render(request, 'blog/home.html')

    else:
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})


