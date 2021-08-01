from socket import *

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 重启释放端口
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

print('server start')
conn, addr = tcp_server.accept()  # 阻塞
print('双向连接是', conn)
print('客户端地址', addr)
while True:
    data = conn.recv(buffer_size)
    print('来自客户端的消息是:', data.decode('utf8'))
    conn.send(data.upper())

conn.close()
tcp_server.close()
