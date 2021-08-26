# ajax.url

from django.conf.urls import url
from ajax import views

urlpatterns = [
    url('ajax1', views.ajax1, name='ajax1'),
    url('ajax2', views.ajax2, name='ajax2')
]

