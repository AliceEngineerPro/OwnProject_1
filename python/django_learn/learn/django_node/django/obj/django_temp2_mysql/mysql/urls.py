# mysql url

from mysql import views
from django.conf.urls import url

urlpatterns = [
    url('index', views.index, name='index'),
    url('', views.home, name='home'),

]
