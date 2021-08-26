# Create your views here.

# views
from classes.models import Classes
from django.shortcuts import render, redirect, HttpResponse
from classes.models import Teachers


def classes(request):
    return render(request, 'home_classes.html')


def select_classes(request):
    classes_list = Classes.objects.all()
    return render(request, 'select_classes.html', {'classes_list': classes_list})


def add_classes(request):
    if request.method == 'GET':
        return render(request, 'add_classes.html')
    elif request.method == 'POST':
        add_name = request.POST.get('id')
        Classes.objects.create(name=add_name)
        return redirect(to=select_classes)


def del_classes(request):
    uid = request.GET.get('uid')
    Classes.objects.filter(id=uid).delete()
    return redirect(to=select_classes)


def update_classes(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        class_msg = Classes.objects.filter(id=uid).get()
        return render(request, 'update_classes.html', {'class_msg': class_msg})
    elif request.method == 'POST':
        # nid = request.POST.get('nid')
        update_msg = request.POST.get('id')
        Classes.objects.filter(id=uid).update(name=update_msg)
        return redirect(to=select_classes)


def allot_teachers(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        classes_msg = Classes.objects.filter(id=uid).get()  # 获取ID对应的班级信息
        # class_teacher_list = classes_msg.classes_and_teachers.all()  # 获取当前ID下所有classes_classes_and_teacher的数据
        class_teacher_list = classes_msg.classes_and_teachers.all().values_list('id')
        id_list = list(zip(*class_teacher_list))[0] if list(zip(*class_teacher_list)) else []
        teachers_list = Teachers.objects.all()
        return render(request, 'add_teacher.html', {'class': id_list, 'teacher': teachers_list, 'uid': uid})
    elif request.method == 'POST':
        uid = request.GET.get('uid')
        teacher_name_list = request.POST.getlist('teacher_id')
        Classes.objects.filter(id=uid).first().classes_and_teachers.set(teacher_name_list)
        return redirect(to=select_classes)
