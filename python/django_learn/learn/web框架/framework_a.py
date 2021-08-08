from wsgiref.simple_server import make_server
import time


def index_404():
    f = open('dj_html/404.html', 'rb')
    data = f.read()
    return data


def foo_alex(req):

    f = open('dj_html/about_alex.html', 'rb')
    data = f.read()
    return data


def foo_other(req):

    f = open('dj_html/about_other.html', 'rb')
    data = f.read()
    return data


def login(req):

    f = open('dj_html/login.html', 'rb')
    data = f.read()
    return data


def signup(req):
    pass


def showtime(req):
    now_time = time.asctime()
    # return b'<h1>%s</h1>' % str(now_time).encode('utf8')

    f = open('dj_html/showtime.html', 'rb')
    data = f.read()
    data = data.decode('utf8')
    data = data.replace('@time@', str(now_time))
    # data.replace('@time@', now_time)
    return data.encode('utf8')


def router():
    url_patterns = [
        ('/login', login),
        ('/signup', signup),
        ('/alex', foo_alex),
        ('/other', foo_other),
        ('/time', showtime),
    ]
    return url_patterns


def application(environ, start_response):

    path = environ['PATH_INFO']
    start_response('200 ok', [('Content-Type', 'text/html')])
    print('path', environ['PATH_INFO'])

    url_patterns = router()

    var_path = None
    for item in url_patterns:
        if item[0] == path:
            var_path = item[1]
            break

    if var_path:
        return [var_path(environ)]
    else:
        return [index_404()]

    # if path == '/alex':
    #     return [foo_alex()]
    # elif path == '/other':
    #     return [foo_other()]
    # else:
    #     return [index_404()]

    # return [b'<h1>Hello Web!</h1>']


httpd = make_server('', 8088, application)

print('Serving HTTP on port 8088...')
httpd.serve_forever()
