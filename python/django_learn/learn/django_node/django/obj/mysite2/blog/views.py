from django.shortcuts import render
from django.shortcuts import HttpResponse
import time


# Create your views here.


def showtime(request):

    now_time = time.asctime()
    # return HttpResponse('hello')

    return render(request, "index.html", {'now_time': now_time})
