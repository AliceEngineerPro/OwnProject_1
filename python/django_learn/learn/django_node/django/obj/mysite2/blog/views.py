import time

from django.shortcuts import HttpResponse
from django.shortcuts import render


# Create your views here.


def home(request):

    name = 'Jack'
    now_time = time.asctime()

    # return HttpResponse('hello')

    # return render(request, "index.html", {'now_time': now_time, 'name': name})
    return render(request, "index.html", locals())


def article_find(request, year):
    return HttpResponse('%s-' % year)


def article_ymd(request, year, month, day):
    return HttpResponse('%s-%s-%s' % (year, month, day))


def signin(request):
    # print(request.path)  # 源路径
    # print(request.get_full_path())  # 带有数据的路径
    if request.method == 'POST':
        return HttpResponse('注册成功')
    return render(request, 'signin.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    # return HttpResponse('登陆成功')


def my_home(request):
    name = request.POST.get('username')
    if name != '':
        return render(request, 'my_home.html', locals())
    return render(request, 'login.html')


