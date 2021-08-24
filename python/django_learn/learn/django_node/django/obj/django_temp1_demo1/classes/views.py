# Create your views here.

# views
from . import models
from django.shortcuts import render, redirect, HttpResponse


def classes(request):
    return render(request, 'home_classes.html')


def select_classes(request):
    classes_list = models.Classes.objects.all()
    return render(request, 'select_classes.html', {'classes_list': classes_list})


def add_classes(request):
    if request.method == 'GET':
        return render(request, 'add_classes.html')
    elif request.method == 'POST':
        add_name = request.POST.get('id')
        models.Classes.objects.create(name=add_name)
        return redirect(to=select_classes)


def del_classes(request):
    uid = request.GET.get('uid')
    models.Classes.objects.filter(id=uid).delete()
    return redirect(to=select_classes)


def update_classes(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        class_msg = models.Classes.objects.filter(id=uid).get()
        return render(request, 'update_classes.html', {'class_msg': class_msg})
    elif request.method == 'POST':
        # nid = request.POST.get('nid')
        update_msg = request.POST.get('id')
        models.Classes.objects.filter(id=uid).update(name=update_msg)
        return redirect(to=select_classes)


