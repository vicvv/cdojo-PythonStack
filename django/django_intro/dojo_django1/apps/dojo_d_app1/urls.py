from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.index),
    url(r'^create$', views.index),
    url(r'^\d+$', views.index),
    url(r'^\d+/edit$', views.index),
    url(r'^\d+/delete$', views.index),

]
