"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URConf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from blog import views

root_dir = views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('home/', views.home),
    url('^blog/', include('blog.urls')),
    url('^login/', views.login, name='login'),
    # url('own/(?P<name>^[a-zA-Z0-9_-]{1,12})/', views.my_home, name='own'),
    # url('own/(?P<name>jack)', views.my_home, name='own'),
    # url('', admin),

]
