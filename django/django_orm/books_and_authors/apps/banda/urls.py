from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^books$', views.books, name="books"),

    url(r'^books/(?P<number>\d+)$', views.show_book, name ="showb"),
    
    url(r'^new_book$', views.new_book, name ="adndb"),
    url(r'^add_author/(?P<number>\d+)$', views.add_author, name = "adda"), 
    url(r'^authors$', views.authors, name="authors"),     
    url(r'^authors/(?P<number>\d+)$', views.show_author, name ="showa"),
    url(r'^new_author$', views.new_author, name="newauthor"),
    url(r'^add_book/(?P<number>\d+)$', views.add_book, name ="addbook"), 
]