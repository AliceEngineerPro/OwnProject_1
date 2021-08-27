from django.shortcuts import render

# Create your views here.

from classes.models import Student, Classes
from django.shortcuts import redirect, HttpResponse


def index(request):
    return render(request, 'index_students.html')


def select_students(request):
    students_list = Student.objects.all()
    return render(request, 'select_students.html', {'students_list': students_list})


def add_students(request):
    if request.method == 'POST':
        name_msg = request.POST.get('name')
        age_msg = request.POST.get('age')
        gender_msg = request.POST.get('gender')
        class_id_msg = request.POST.get('class_id')
        Student.objects.create(name=name_msg, age=age_msg, gender=gender_msg, classes_to_student_id=class_id_msg)
        return redirect(to=select_students)
    elif request.method == 'GET':
        classes_msg = Classes.objects.all()
        return render(request, 'add_students.html', {'classes_msg': classes_msg})


def del_students(request):
    uid = request.GET.get('uid')
    Student.objects.filter(id=uid).delete()
    return redirect(to=select_students)


def update_students(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        students_list = Student.objects.filter(id=uid).get()
        classes_msg = Classes.objects.all()
        print(students_list.name, classes_msg)
        return render(request, 'update_students.html', {'students_list': students_list, 'classes_msg': classes_msg})
    if request.method == 'POST':
        uid = request.GET.get('uid')
        name_msg = request.POST.get('name')
        age_msg = request.POST.get('age')
        gender_mag = request.POST.get('gender')
        class_id_msg = request.POST.get('class_id')
        Student.objects.filter(id=uid).update(name=name_msg, age=age_msg, gender=gender_mag,
                                              classes_to_student=class_id_msg)
        print(uid, name_msg, age_msg, gender_mag, class_id_msg)
        return redirect(to=select_students)


def ajax_del_students(request):
    nid = request.GET.get('nid')
    msg = '成功'
    try:
        Student.objects.filter(id=nid).delete()
    except Exception as e:
        msg = str(e)
    return HttpResponse(msg)
