import time
import socket
import threading


class Client:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 2000
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            msg = input(">>")
            self.client_socket.send(msg.encode("utf-8"))

    def recvMsg(self):
        while True:
            msg = self.client_socket.recv(1024)
            print(msg.decode())

    def config(self):
        self.client_socket.connect((self.ip, self.port))

    def start(self):
        self.config()

        t1 = threading.Thread(target=self.sendMsg, args=())
        t2 = threading.Thread(target=self.recvMsg, args=())

        t1.start()
        t2.start()


if __name__ == '__main__':
    client = Client()
    client.start()
