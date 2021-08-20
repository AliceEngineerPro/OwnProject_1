from django.shortcuts import render

# Create your views here.


def backend(request):
    return render(request, 'index.html')


def student(request):
    student_list = ['Jack', 'Alex', 'Steven']
    return render(request, 'student.html', locals())
