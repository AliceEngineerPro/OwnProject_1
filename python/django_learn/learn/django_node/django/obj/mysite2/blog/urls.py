from blog import views
from django.conf.urls import url

urlpatterns = [
    url('article/(\d{4})$', views.article_find),
    url('article/(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})', views.article_ymd),
    url('signin/', views.signin, name='signin'),

]
