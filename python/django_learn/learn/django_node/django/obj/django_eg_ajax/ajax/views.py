from django.shortcuts import render

# Create your views here.

from ajax import models
from django.shortcuts import redirect, HttpResponse
import json


def student(request):
    if request.method == 'GET':
        student_list = models.Student.objects.all()
        class_list = models.Classes.objects.all()
        return render(request, 'student.html', locals())
    elif request.method == 'POST':
        return_value = {'status': True, 'message': None, 'data': None}
        try:
            s_name = request.POST.get('name')
            s_age = request.POST.get('age')
            s_gender = request.POST.get('gender')
            s_class_id = request.POST.get('class_id')
            a_student = models.Student.objects.create(name=s_name, age=s_age, gender=s_gender, classes_id=s_class_id)
            return_value['data'] = a_student.id
        except Exception as e:
            return_value['status'] = False
            return_value['message'] = '内容输入错误'
        result = json.dumps(return_value, ensure_ascii=False)
        return HttpResponse(result)


def delete(request):
    s_id = request.GET.get('nid')
    models.Student.objects.filter(id=s_id).delete()
    return redirect(to=student)
