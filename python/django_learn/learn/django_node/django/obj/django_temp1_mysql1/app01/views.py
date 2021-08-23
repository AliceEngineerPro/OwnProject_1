# Create your views here.
from app01 import models
from django.shortcuts import HttpResponse
from django.shortcuts import render

publish = models.Publish
book = models.Book
author = models.Author
book_author = models.BookAndAuthor


def index(request):
    return render(request, 'index.html')


def add_data(request):
    # publish.objects.create(name='人民出版社', city='北京')
    # publish.objects.create(name='机械出版社', city='北京')
    # publish.objects.create(name='南方出版社', city='南京')
    # publish.objects.create(name='河北出版社', city='河北')
    return HttpResponse('添加成功')


def add_book(request):
    # book.objects.create(name='python', price=69, date=datetime.date.today(), publish_id=3)
    # book.objects.create(name='linux', price=88, date=datetime.date.today(), publish_id=2)
    # book.objects.create(name='java', price=178, date=datetime.date.today(), publish_id=1)
    # book.objects.create(name='go', price=588, date=datetime.date.today(), publish_id=4)
    # book.objects.create(name='django', price=588, date=datetime.date.today(), publish_id=3)

    return HttpResponse('添加成功')


def add_author(request):
    author.objects.create(name='Alex', age=27)
    author.objects.create(name='Jack', age=40)
    author.objects.create(name='Steven', age=30)

    return HttpResponse('添加成功')


def select(request):
    # 一对一
    # book_obj = book.objects.get(name='django')
    # print(book_obj.publish)
    # print(book_obj.publish.name, book_obj.publish.city)

    # pub = publish.objects.filter(name='人民出版社')[0]
    # book_pub = book.objects.filter(publish=pub).values('name', 'price')
    # print(book_pub)

    # pub = publish.objects.filter(name='人民出版社')[0]
    # print(pub.book_set.all().value('name', 'price'))

    # 一对多
    # ret1 = book.objects.filter(publish__name='南方出版社').values('name', 'price')
    # ret2 = publish.objects.filter(book__name='python').values('name', 'city')
    # ret3 = book.objects.filter(name='python').values('name', 'publish__name', 'publish__city')
    # ret4 = book.objects.filter(publish__city='北京').values('name', 'price')
    # print(ret1)
    # print(ret2)
    # print(ret3)
    # print(ret4)
    # ret5 = book.objects.filter(date__gt='2020-01-01', date__lt='2021-01-01')
    # print(ret5)

    # 多对多
    # book_obj = book.objects.get(id=3)
    # author_msg = book_obj.author.all()
    # print(author_msg)
    # author_obj = author.objects.get(id=2)
    # author_msg = author_obj.book_set.all()
    # print(author_msg)

    # 多对多外键
    # obj1 = book.objects.get(name='linux')
    # print(obj1.bookandauthor_set.all())
    # print(obj1.bookandauthor_set.all()[0].author)
    # obj2 = book.objects.filter(bookandauthor__author__name='Jack').values('name', 'price')
    # for i in obj2:
    #     print(i)
    #     for j in i.values():
    #         print(j)
    # print(obj2[0]['name'])
    # print(obj2[0])

    # 高级查询
    # ret_1 = book.objects.all().aggregate(Avg('price'))  # 平均值
    # print(ret_1)
    # ret_2 = book.objects.filter(bookandauthor__author__name='steven').aggregate(Sum('price'))  # 和
    # print(ret_2)
    # ret_3 = book.objects.values('bookandauthor__author').annotate(Sum('price'))
    # print(ret_3)
    # ret4 = publish.objects.values('name').annotate(Min('book__price'))
    # print(ret4)

    # ret_1 = book.objects.filter(name='linux', price=178)
    # print(ret_1)
    # Q 方法查询
    # ret_2 = book.objects.filter(Q(price=618) | Q(name='python'))   # or 或 查询
    # print(ret_2)
    # ret_3 = book.objects.filter(~Q(price__gt=100)).values('name', 'price')  # not 非 查询
    # print(ret_3)

    # querySet 查询方法
    ret_4 = book.objects.filter(price__gt=150)
    ret_5 = ret_4.iterator()
    for i in ret_5:
        print(i.name)

    return HttpResponse('查询成功')


# 多对多绑定
def related(request):
    # 通过对象manytomany创建
    # book_obj = book.objects.get(name='python')
    # author_obj = author.objects.all()
    # book_obj.author.add(*author_obj)

    # 通过 外键手工创建多对多
    # book_author.objects.create(book_id=2, author_id=3)
    # book_author.objects.create(book_id=2, author_id=2)
    # book_author.objects.create(book_id=5, author_id=2)
    # book_author.objects.create(book_id=4, author_id=2)

    return HttpResponse('绑定成功')


def update(request):
    # ret_1 = book.objects.all().values('name', 'price')
    # for i in ret_1:
    #     book.objects.filter(name=i['name']).update(price=i['price'] + 10)

    # F
    # book.objects.all().update(price=F('price') + 10)
    return HttpResponse('修改成功')
