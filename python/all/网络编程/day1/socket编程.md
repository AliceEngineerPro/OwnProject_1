# **<font color=red>socket编程</font>**
## OSI七层

![](https://amfc-1301595111.cos.ap-chengdu.myqcloud.com/learn/python/%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B/OSI%E4%B8%83%E5%B1%82.jpg)

### 1. socket编程

![](https://amfc-1301595111.cos.ap-chengdu.myqcloud.com/learn/python/%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B/socket1.jpg)

- **socket层**

![](https://amfc-1301595111.cos.ap-chengdu.myqcloud.com/learn/python/%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B/socket2.jpg)

- **socket套接字工作流程**

![](https://amfc-1301595111.cos.ap-chengdu.myqcloud.com/learn/python/%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B/socket%E5%A5%97%E6%8E%A5%E5%AD%97.jpg)

```python
# server
import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8000))

phone.listen(5)

conn, addr = phone.accept()  # 等电话

msg = conn.recv(1024)  # 收消息
print('客户端发来的消息是:', msg)

conn.send(msg.upper())
conn.close()
phone.close()


# client
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8000))  # 拨通电话
phone.send('hello'.encod('utf8'))
data = phone.recv(1204)
print('收到服务端发来的消息')
```

- **三次握手/四次挥手**

![](https://amfc-1301595111.cos.ap-chengdu.myqcloud.com/learn/python/%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B/tcp%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B%E5%92%8C%E5%9B%9B%E6%AC%A1%E6%8C%A5%E6%89%8B.jpg)

- **socket原理**

![](https://cos.amfc.ltd/learn/python/%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B/socket%E5%8E%9F%E7%90%861.jpg)

  - Server

```python
# tcp server
from socket import *
ip_server = ('127.0.0.1', 8080)
buff_size = 1024
ss = socket()  # 创建服务器套接字
ss.bind(ip_server)  # 把地址绑定到套接字
while True:  # 服务器无限循环
    cs = ss.accept()
    while True:  # 通讯循环
        comm = ss.recv(bufsize=buff_size)  # 对话/接受
        conn = ss.send(bifsize.decode('utf8'))  # 对话/发送
    cs.close()  # 关闭套接字
```

  - Client

```python
# tcp Client
from socket import *
ip_client = ('127.0.0.1', 8080)
buff_size = 1024
cs = socket()  # 创建客户端套接字
cs.connect(ip_client)  # 连接到服务端
while True:  # 通讯循环
    cs.send(buff_size.decode('utf8')) # 发送
    cs.recv(bufsize=buff_size)  # 接受

cs.close()  # 关闭
```
