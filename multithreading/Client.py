import socket
import time

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 2000

# 连接服务，指定主机和端口
s.connect(("127.0.0.1", port))

while True:
    s.send("hello".encode("utf-8"))
    # 接收小于 1024 字节的数据
    msg = s.recv(1024)
    print(msg.decode('utf-8'))
    time.sleep(2)
