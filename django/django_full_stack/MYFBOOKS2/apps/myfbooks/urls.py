from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home$', views.home,  name="home"),
    url(r'^about$', views.about,  name="about"),
    url(r'^newbook$', views.newbook,  name="newbook"),
    url(r'^newbook/newbookform$', views.newbookform),
    url(r'^home/(?P<book_id>\d+)/likebook$', views.likebook,name = 'like'),
    url(r'^home/(?P<book_id>\d+)/unlikebook$', views.unlikebook,name = 'unlike'),

    url(r'^home/(?P<book_id>\d+)/view$', views.viewbook,name="view"), 
    url(r'^home/(?P<book_id>\d+)/edit$', views.editbook,name ='edit'),
    url(r'^home/(?P<book_id>\d+)/edit/process$', views.process_edit),
    url(r'^home/(?P<book_id>\d+)/delete$', views.deletebook, name= 'delete'), 

]
