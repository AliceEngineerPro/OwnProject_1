from django.shortcuts import render

# Create your views here.

from ajax import models


def student(request):
    student_list = models.Student.objects.all()
    return render(request, 'student.html', locals())
