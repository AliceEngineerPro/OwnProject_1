# web框架


**框架**:framework,特指为解决一个开放性问题而设计的具有一定约束性的支撑结构，使用框架可以帮你快速开发特定的系统，简单地说，就是你用别人搭建好的舞台来做表演  
对于所有的web框架，本质上其实就是一个socket服务端，用户的浏览器其实就是一个socket客户端

<hr>

- 最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回  
- 如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读HTTP规范  
- 正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务  
- <font color=red>这个接口就是WSGI：Web Server Gateway Interface</font>  
<hr>

```python
from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


httpd = make_server('', 8080, application)

print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
```

<hr>

- framework

```python
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
```

- about.alex

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About</title>
</head>
<body>
<h1>Hello Alex</h1>
</body>
</html>
```

- about.other

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About</title>
</head>
<body>
<h1>hello other</h1>
</body>
</html>
```

- login

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>login</title>
</head>
<body>
<form action="http://127.0.0.1:8088/alex" method="post">
    <p><label for="username">用户名</label><input type="text" name="username" id="username"></p>
    <p><label for="password">密码</label><input type="password" name="password" id="password"></p>
    <p><input type="submit" name="login" id="login"></p>
      </form>
      </body>
</html>
```

- 404

```html
<!DOCTYPE html>
<html lang="zh">

<head>
    <meta charset="utf-8">
    <title>404</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0"/>
    <style>
        html,
        body {
            width: 100%;
            height: 100%
        }

        a,
        a img,
        a:before,
        a:after {
            text-decoration: none;
            transition-duration: .25s
        }

        section {
            display: block
        }

        body {
            line-height: 1
        }

        #about {
            width: 40%;
            position: absolute;
            top: 40%;
            left: 10%;
            z-index: 20;
            transform: translate(0, -50%);
        }

        #about h1 {
            margin: 30px;
        }

        #about p {
            margin: 30px;
        }

        #about img {
            margin-left: 30px;
        }

        #about .social {
            float: left;
            margin: 30px;
        }

        #about .copyright {
            width: 100%;
            float: left;
            margin-bottom: 0px;
        }

        @media (max-width: 768px) {
            #about {
                width: 100%;
                left: 0px;
                height: 100%;
                background-color: rgba(255, 255, 255, 0.85);
            }

            #about h1 {
                margin: 30px;
            }

            #about p {
                margin: 30px;
            }

            #about .social {
                margin: 30px;
            }

            #about .copyright {
                width: 100%;
                float: left;
                margin-bottom: 0;
            }
        }

        @media (max-width: 580px) {
            #about {
                width: 100%;
                left: 0;
                height: 100%;
                background-color: rgba(255, 255, 255, 0.85);
            }

            #about h1 {
                margin: 30px;
            }

            #about p {
                margin: 30px;
                margin-bottom: 0
            }

            #about .social {
                margin: 30px;
                margin-bottom: 0
            }

            #about .copyright {
                width: 100%;
                float: left;
                margin-bottom: 0;
            }
        }

        .animated {
            animation-duration: 1s;
            animation-fill-mode: both
        }

        .bounce-in {
            animation-name: bounce-in
        }

        @keyframes bounce-in {
            from,
            60%,
            75%,
            90%,
            to {
                animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1)
            }
            0% {
                opacity: 0;
                transform: translate3d(-3000px, -50%, 0)
            }
            60% {
                opacity: 1;
                transform: translate3d(25px, -50%, 0)
            }
            75% {
                transform: translate3d(-10px, -50%, 0)
            }
            90% {
                transform: translate3d(5px, -50%, 0)
            }
            to {
                transform: translate3d(0, -50%)
            }
        }

        body {
            font-family: "Roboto", sans-serif;
            font-size: 16px;
            font-weight: 300;
            line-height: 1.75;
            color: rgba(0, 0, 0, 0.65)
        }

        h1 {
            font-family: "Merriweather", sans-serif;
            font-size: 50px;
            font-weight: 700;
            line-height: 1.25;
            color: rgba(0, 0, 0, 0.85);
            margin-bottom: 25px
        }

        a {
            color: rgba(3, 3, 3, 0.85);
            font-weight: 600;
        }

        @media (max-width: 580px) {
            body {
                font-size: 14px
            }

            h1 {
                font-size: 42px;
                line-height: 1.45
            }
        }

        .bg-align {
            margin-top: 50%;
        }
    </style>
</head>
<body>
<section id="about" class="animated bounce-in">
    <div class="bg-align">
        <h1>404</h1>
        <p>Oops! It looks like you're lost...</p>
        <p>The Page you're looking for doesn't exist or another error occurred.</p>
    </div>
</section>
</body>
</html>
```

- showtime

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>时间</title>
</head>
<body>
<h1>时间: @time@</h1>
</body>
</html>
```
