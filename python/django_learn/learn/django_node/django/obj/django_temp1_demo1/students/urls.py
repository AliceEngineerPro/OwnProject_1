from django.conf.urls import url

from . import views


urlpatterns = [
    url('index/', views.index, name='index'),
    url('select/', views.select_students, name='select_students'),
    url('add/', views.add_students, name='add_students')

]
