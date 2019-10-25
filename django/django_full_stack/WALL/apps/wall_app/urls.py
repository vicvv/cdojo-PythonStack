from django.conf.urls import url,include
from django.contrib import admin
from  .  import views

urlpatterns = [
    url(r'^$', views.index),   
    url(r'^home$', views.home, name = "home"),
    url(r'^home/about$', views.about, name = 'about'),

    url(r'^home/newpost$', views.newpost, name = 'newpost'),
    url(r'^home/newcomentform$', views.newcomentform,),
    url(r'^home/newpost/newpostform$', views.newpostform ),

    url(r'^home/(?P<post_id>\d+)/editpost$', views.editpost, name = 'edit'),    
    url(r'^home/(?P<post_id>\d+)/editpost/editpostform$',views.editpostform),
    url(r'^home/(?P<post_id>\d+)/delete$', views.deletemessage, name= 'delete'),   
]
