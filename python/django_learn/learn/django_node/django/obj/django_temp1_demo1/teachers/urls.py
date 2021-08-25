# teachers

from django.conf.urls import url
from teachers import views


urlpatterns = [
    url('index', views.index_teacher, name='index_teacher'),
    url('select', views.select_teacher, name='select_teacher'),
    url('add', views.add_teacher, name='add_teacher'),
    url('del', views.del_teacher, name='del_teacher'),
    url('update', views.update_teacher, name='update_teacher')
]
