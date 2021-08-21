from django.db import models

# Create your models here.


class Publish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24, null=False,)
    city = models.CharField(max_length=24, null=False, default='中国')

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    price = models.IntegerField()
    date = models.DateField()
    publish = models.ForeignKey(db_column='publish_id', to='Publish', on_delete=models.CASCADE)
    # author = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.name


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class BookAndAuthor(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE)


