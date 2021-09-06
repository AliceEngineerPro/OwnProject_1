from django.db import models

# Create your models here.


class Classes(models.Model):
    """
    班级表
    """
    name = models.CharField(max_length=24)
    to_teachers = models.ManyToManyField(db_column='teacher_id', to='Teachers')


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
    classes = models.ForeignKey(db_column='class_id', to='Classes', on_delete=models.CASCADE)
