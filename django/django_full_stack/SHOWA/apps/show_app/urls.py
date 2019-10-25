from django.conf.urls import url , include
from  .  import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^shows$', views.shows),
    url(r'^shows/new$', views.new_show,name="new"),
    url(r'^shows/new/add$', views.add_new_show),
    url(r'^shows/(?P<show_id>\d+)$', views.view_show, name="view"),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit_show,name="edit"),
    url(r'^shows/(?P<show_id>\d+)/edit/process$', views.process_edit),
    url(r'^shows/(?P<show_id>\d+)/delete$', views.remove_show, name ="delete")
]