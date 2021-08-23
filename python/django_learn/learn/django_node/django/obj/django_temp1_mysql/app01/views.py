from app01 import models
# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render

book = models.Book


def index(request):
    return render(request, 'index.html')


def add_book(request):
    # 实例化对象
    # add = book(name='python', price=99, author='Jack', up_date='2021-08-21')
    # add.save()

    # 调用 objects
    book.objects.create(name='Linux', price=199, author='Alex', up_date='2017-06-06')
    # book.objects.create(name='Python', price=89, author='Jack', up_date='2021-02-13')
    # book.objects.create(name='Django', price=179, author='Other', up_date='2019-08-16')
    # book.objects.create(name='MySQL', price=139, author='Alex', up_date='2020-11-30')
    # book.objects.create(name='Html', price=30, author='Jack', up_date='2012-01-03')
    # book.objects.create(name='Css', price=50, author='Steven', up_date='2019-08-16')

    return HttpResponse("添加成功")


def mod_book(request):
    # 调用 objects
    book.objects.filter(author='Jack', name='Python').update(price='139')

    # get 方法只能调用一个对象(该对象是实例对象)
    # mod = book.objects.get(author='Jack')
    # # print(mod, type(mod))  # <QuerySet [<Book: Book object (1)>]> <class 'django.db.models.query.QuerySet'>
    # mod.price = 120
    # mod.save()

    return HttpResponse('修改成功')


def del_book(request):
    # 调用 objects
    book.objects.filter(name='python').delete()

    return HttpResponse('删除成功')


def sel_book(request):  # book_list 可以遍历, book_msg 为一条记录
    # 全部查询, [:3]-->切片
    # book_list = book.objects.all()[:3]
    # book_list = book.objects.all()[::-1]
    # 条件查询
    # book_list = book.objects.filter(author='Alex').all()
    # book_list = book.objects.filter(author='Alex').values()
    # book_list = book.objects.filter(price__gt=150)
    book_list = book.objects.filter(name__icontains='n').distinct().values('name', 'price', 'author')
    # 去重
    # book_list = book.objects.filter(author='Alex').distinct().values('name', 'price', 'author')

    # 第一条数据
    # book_msg = book.objects.first()
    # 最后一条数据
    # book_msg = book.objects.last()
    # 只能取一条数据
    book_msg = book.objects.get(name='Html')
    print(book_list)
    print(book_msg)
    return render(request, 'index.html', locals())
