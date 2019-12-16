from multithreading.Client import Client
from time import sleep
from random import uniform
import multiprocessing
import hashlib


def hh(i):
    md5 = hashlib.md5()
    md5.update(str(i).encode('utf-8'))
    return md5.hexdigest()


class MultiClient(Client):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def config(self):
        self.client_socket.bind((self.ip, int(self.name) + 2001))
        self.client_socket.connect((self.ip, self.port))

    def sendMsg(self):
        while True:
            sleep(uniform(0, 1))
            msg = "hello from {}".format(hh(self.name))
            self.client_socket.send(msg.encode("utf-8"))


if __name__ == '__main__':
    p = multiprocessing.Pool(10)

    for i in range(10):
        client = MultiClient(i)
        sleep(0.5)
        p.apply_async(client.start, )

    print("init success!")

    p.close()
    p.join()
