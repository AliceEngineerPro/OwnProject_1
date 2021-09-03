from django.conf.urls import url
from ajax import views


urlpatterns = [
    url('student/', views.student, name='student'),
]
