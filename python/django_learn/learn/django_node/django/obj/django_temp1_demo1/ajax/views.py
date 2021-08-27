from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse, redirect
import time


def ajax1(request):
    return render(request, 'ajax1.html')


def ajax2(request):
    user = request.GET.get('user')
    passwd = request.GET.get('passwd')
    time.sleep(5)
    return HttpResponse('ok',)


def ajax3(request):
    num_1 = int(request.POST.get('v1'))
    num_2 = int(request.POST.get('v2'))
    try:
        msg = num_1 + num_2
    except Exception as e:
        msg = '输入格式错误'
    return HttpResponse(msg)