from socket import *

ip_port = ('server.amfc.ltd', 8000)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    msg = input('>>:').strip()
    tcp_client.send(msg.encode('utf8'))
    print('客户端已经发送消息')
    data = tcp_client.recv(buffer_size)
    print('收到服务器发来的消息', data.decode('utf8'))

tcp_client.close()
