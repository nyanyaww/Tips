import socket
import threading


class Server:

    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 2000
        self.listen_size = 5
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_list = []

    def sendMsg(self):
        while True:
            msg = input(">>")
            if len(self.client_list) != 0:
                for each in self.client_list:
                    each.send(msg.encode('utf-8'))

    def listenClient(self):
        while True:
            # 建立客户端连接
            client_socket, addr = self.server_socket.accept()
            print("连接地址:{}".format(str(addr)))
            if client_socket not in self.client_list:
                self.client_list.append(client_socket)

    def recvMsg(self):
        while True:
            for each_client_socket in self.client_list:
                try:
                    data = each_client_socket.recv(1024)
                    print(data.decode())
                    # echo
                    msg = data.decode()
                    each_client_socket.send(msg.encode('utf-8'))
                except IOError:
                    print("没了")
                    each_client_socket.close()

    def config(self):
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(self.listen_size)

    def start(self):
        self.config()
        t1 = threading.Thread(target=self.sendMsg, args=())
        t2 = threading.Thread(target=self.listenClient, args=())
        t3 = threading.Thread(target=self.recvMsg, args=())

        t1.start()
        t2.start()
        t3.start()


if __name__ == '__main__':
    server = Server()
    server.start()
