from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^$', views.index),
    url(r'^home$', views.home, name = 'blog-home'), 
    url(r'^about$', views.about, name= 'blog-about') ,  
]
