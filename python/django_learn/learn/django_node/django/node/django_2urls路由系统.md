# Django URL (路由系统)

URL配置(URLconf)就像Django 所支撑网站的目录。它的本质是URL模式以及要为该URL模式调用的视图函数之间的映射表；你就是以这种方式告诉Django，对于这个URL调用这段代码，对于那个URL调用那段代码。

```bash
urlpatterns = [
    url(正则表达式, views视图函数，参数，别名),
]
```

- 参数说明
  - 一个正则表达式字符串
  - 一个可调用对象，通常为一个视图函数或一个指定视图函数路径的字符串
  - 可选的要传递给视图函数的默认参数（字典形式）
  - 一个可选的name参数

## URLconf

```python
from django.conf.urls import url
from django.contrib import admin

from app01 import views

urlpatterns = [

    url(r'^articles/2003/$', views.special_case_2003),

    #url(r'^articles/[0-9]{4}/$', views.year_archive),

    url(r'^articles/([0-9]{4})/$', views.year_archive),  #no_named group

    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),

    url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),

]
```

