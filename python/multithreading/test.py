# -*- coding: utf-8 -*-

# 消息发布/订阅模型

from collections import defaultdict
from contextlib import contextmanager


class Exchange(object):
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, message):
        for subscriber in self._subscribers:
            subscriber.send(message)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)


_exchanges = defaultdict(Exchange)


def get_exchange(name):
    return _exchanges[name]


class Task(object):
    def send(self, message):
        """发送消息的方法"""
        print(message)


task1 = Task()
task2 = Task()


# 1、手动 添加注册，取消注册
exchage = get_exchange("message")
exchage.attach(task1)
exchage.attach(task2)

exchage = get_exchange("message")
exchage.send("你好")
# 你好
# 你好

exchage.detach(task1)
exchage.detach(task2)

# 2、使用上下文管理器

exchage = get_exchange("message")
with exchage.subscribe(task1, task2):
    exchage.send("你好啊")

