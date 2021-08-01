from socket import *


def main():

    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(('localhost', 5432))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        buf = connection.recv(1024)
        f = open('E:\Self_file\self_git\VScodeNote\html\html_code\1.html', 'rb')
        data = f.read()
        connection.sendall(bytes('HTTP/1.1 201 OK\r\n\r\n', 'utf8'))

        connection.sendall(data)

        connection.close()


if __name__ == '__main__':

    main()
