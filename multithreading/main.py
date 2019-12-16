import threading


class Server:

    def __init__(self):
        pass

    def sendMsg(self):
        pass

    def recvMsg(self):
        pass

    def start(self):
        t1 = threading.Thread(target=self.sendMsg, args=())
        t2 = threading.Thread(target=self.recvMsg, args=())

        t1.start()
        t2.start()


if __name__ == '__main__':
    pass
