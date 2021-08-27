from django.conf.urls import url

from . import views


urlpatterns = [
    url('index/', views.index, name='index'),
    url('select/', views.select_students, name='select_students'),
    url('add/', views.add_students, name='add_students'),
    url('del/', views.del_students, name='del_students'),
    url('update/', views.update_students, name='update_students'),
    url('ajax_del_students/', views.ajax_del_students, name='ajax_del_students'),
]
