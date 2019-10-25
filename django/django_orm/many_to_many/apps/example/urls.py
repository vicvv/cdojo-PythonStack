from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'books$', views.books), 
    url(r'authors/add_author$', views.authors),  
    url(r'authors$', views.authors), 
    url(r'$', views.index),
]