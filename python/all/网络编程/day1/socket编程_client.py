import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8000))  # 拨通电话
phone.send('hello'.encode('utf8'))
data = phone.recv(1204)
print('收到服务端发来的消息')

