# Create your models here.
from django.db import models


class Classes(models.Model):
    """
    班级表
    """
    name = models.CharField(max_length=24)
    classes_and_teachers = models.ManyToManyField(to='Teachers')


class Teachers(models.Model):
    """
    老师表
    """
    name = models.CharField(max_length=24)


class Student(models.Model):
    """
    学生表
    """
    name = models.CharField(max_length=24)
    age = models.IntegerField()
    gender = models.BooleanField()
    classes_to_student = models.ForeignKey(db_column='classes_id', to='Classes', on_delete=models.CASCADE)
