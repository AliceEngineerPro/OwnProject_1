# classes/*

from django.conf.urls import url
from . import views


urlpatterns = [
    url('index', views.classes, name='classes'),
    url('select/', views.select_classes, name='select_class'),
    url('add/', views.add_classes, name='add_class'),
    url('del', views.del_classes, name='del_classes'),
    url('update', views.update_classes, name='update_classes')

]
