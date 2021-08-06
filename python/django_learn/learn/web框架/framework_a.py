from wsgiref.simple_server import make_server


def application(environ, start_response):
    print(environ)
    start_response('200 ok', [('Content-Type', 'text/html')])
    return [b'<h1>Hello Web!</h1>']


httpd = make_server('', 8088, application)

print('Serving HTTP on port 8088...')
httpd.serve_forever()
