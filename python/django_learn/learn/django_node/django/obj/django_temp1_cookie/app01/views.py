from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse, redirect


def login(request):
    print('cookie', request.COOKIES)  # 字典
    print('session', request.session)  # 字典对象

    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        if name == 'admin' and pwd == 'admin':
            return_value = redirect('/index')
            # cookie 设置
            return_value.set_cookie('username', name, max_age=10)  # max_age 为cookie的有效时间

            # session设置
            request.session['is_login'] = True
            request.session['username'] = name

            return return_value

    return render(request, 'login.html')


def index(request):
    # cookie 判断
    if request.COOKIES.get('username', None) == 'admin':
        name = request.COOKIES.get('username', None)
        return render(request, 'index.html', locals())

    # session 判断
    # if request.session.get('is_login', None):  # 默认等于True
    #     name = request.session.get('username')
    #     return render(request, 'index.html', locals())

    else:
        return redirect('/login/')
