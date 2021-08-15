#  django_提交数据并展示(数据库)

- index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>创建个人信息</h1>

<form action="/userInfor/" method="post">

    <p>姓名<input type="text" name="username"></p>
    <p>性别<input type="text" name="sex"></p>
    <p>邮箱<input type="text" name="email"></p>
    <p><input type="submit" value="submit"></p>

</form>

<hr>

<h1>信息展示</h1>

<table border="1">

    <tr>
        <td>姓名</td>
        <td>性别</td>
        <td>邮箱</td>
    </tr>
    {% for i in info_list %}

        <tr>
            <td>{{ i.username }}</td>
            <td>{{ i.sex }}</td>
            <td>{{ i.email }}</td>
        </tr>

    {% endfor %}

</table>

</body>
</html>
```

- models.py

```python
from django.db import models

# Create your models here.


class UserInfor(models.Model):

    username=models.CharField(max_length=64)
    sex=models.CharField(max_length=64)
    email=models.CharField(max_length=64)
```

- views.py

```python
from django.shortcuts import render

from app01 import models
# Create your views here.


def userInfor(req):

    if req.method=="POST":
        u=req.POST.get("username",None)
        s=req.POST.get("sex",None)
        e=req.POST.get("email",None)


       #---------表中插入数据方式一
            # info={"username":u,"sex":e,"email":e}
            # models.UserInfor.objects.create(**info)

       #---------表中插入数据方式二
        models.UserInfor.objects.create(
            username=u,
            sex=s,
            email=e
        )

        info_list=models.UserInfor.objects.all()

        return render(req,"userInfor.html",{"info_list":info_list})

    return render(req,"userInfor.html")
```
