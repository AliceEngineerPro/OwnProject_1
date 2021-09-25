from django.conf.urls import url
from ajax import views
from django.urls import path


urlpatterns = [
    # path('^student/', views.student, name='student'),
    url('^query', views.student, name='student'),
    url('^del/', views.delete, name='delete'),
    url('^del#ajax/', views.delete_ajax, name='delete_ajax'),
    url('^change#ajax/', views.change_ajax, name='change_ajax'),
]
