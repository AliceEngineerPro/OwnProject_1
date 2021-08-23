import datetime
# Create your views here.
import time

from django.shortcuts import HttpResponse
from django.shortcuts import render


def showtime(request):
    now_time = time.asctime()
    return render(request, 'showtime.html', {'now_time': now_time})


class Animal:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


def query(request):

    l = ['Jack', 'Alex']
    # l = []

    d = {'name': 'Jack', 'age': 40, 'hobby': '女'}

    c = Animal('Pig', 'man')

    test = 'hello world'

    num = 10

    t = datetime.datetime.now()

    null = []

    a = '<a href="">click</a>'

    return render(request, 'index.html', locals())


def login(request):
    return HttpResponse('ok')


