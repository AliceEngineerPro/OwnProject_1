# classes/*

from django.conf.urls import url
from . import views


urlpatterns = [
    url('/', views.classes, name='classes'),
    url('select/', views.select_class, name='select_class'),
    url('add/', views.add_class, name='add_class'),

]
