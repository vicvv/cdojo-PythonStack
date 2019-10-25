from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [  
    url(r'register$', views.register, name = 'register'),
    url(r'login$', auth_views.login.as_view(template_name = 'users/login.html'), name='login'),
    url(r'logout$', views.register, name = 'logout'),
   
]