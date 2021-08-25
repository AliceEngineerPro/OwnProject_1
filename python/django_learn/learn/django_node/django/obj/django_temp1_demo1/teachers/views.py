from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse, redirect
from classes.models import Teachers, Classes


def index_teacher(request):
    return render(request, 'index_teachers.html')


def add_teacher(request):
    pass


def select_teacher(request):
    teachers_mag = Classes.objects.all()
    for i in teachers_mag:
        print(i.name, i.classes_and_teachers.all())
    return render(request, 'select_teachers.html', {'teachers_mag': teachers_mag})


def del_teacher(request):
    pass


def update_teacher(request):
    pass
