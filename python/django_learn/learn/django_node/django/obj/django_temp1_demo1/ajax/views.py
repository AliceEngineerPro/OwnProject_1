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
