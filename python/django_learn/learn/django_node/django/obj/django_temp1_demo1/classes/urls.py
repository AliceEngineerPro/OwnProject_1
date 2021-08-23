from django.conf.urls import url
from . import views


urlpatterns = [
    url('select/', views.select_class, name='select_class'),
    url('add/', views.add_class, name='add_class'),
    url('del', views.del_class, name='del_class')

]
