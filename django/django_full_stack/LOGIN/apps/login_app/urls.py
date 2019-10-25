from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
     url(r'^$', views.index, name = 'index'),
     url(r'^logmein$', views.logmein,name = 'login_register'),
     url(r'^logmein/register$', views.register),
     url(r'^logmein/login$', views.login), 
     url(r'^logmein/success$', views.success,name = 'success'), 
     url(r'^logmein/logout$', views.logout, name = 'logout'),   
]