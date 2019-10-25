from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
     url(r'^$', views.index, name = 'index'),
     url(r'^logmein$', views.logmein,name = 'register'),
     url(r'^logmein/register$', views.register),
     url(r'^logmein/login$', views.loginpage, name='login'),
     url(r'^logmein/loginform$', views.login),  
     url(r'^logmein/logout$', views.logout, name = 'logout'),   
]