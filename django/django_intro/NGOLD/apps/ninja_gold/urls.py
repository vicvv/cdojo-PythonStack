from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'process_money$', views.process_money,name="process_money"),
    url(r'$', views.index)
]
