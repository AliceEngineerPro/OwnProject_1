from django.shortcuts import render ,HttpResponse

# Create your views here.


def index(req):

    print('GET', req.GET)
    print('POST', req.POST)

    print('FILES', req.FILES)

    for item in req.FILES:
        file_obj = req.FILES.get(item)
        f = open(file_obj.name, 'wb')
        iter_file = file_obj.chunks()
        for line in iter_file:
            f.write(line)
        f.close()

    return HttpResponse('注册成功')
