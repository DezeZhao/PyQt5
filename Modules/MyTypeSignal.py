# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 22:43
# @Software: PyCharm
# @File    : MyTypeSignal.py
# @Author  : DezeZhao
"""

自定义信号与槽
实现不同对象之间的信号传递
"""
from PyQt5.QtCore import *


class MyTypeSignal(QObject):
    # 定义一个信号
    sendmsg = pyqtSignal(object)

    def run(self):
        # 触发信号
        self.sendmsg.emit('hello pyqt5')


class MySlot(QObject):
    def get(self, msg):
        print(msg)


if __name__ == '__main__':
    send = MyTypeSignal()
    slot = MySlot()
    # 槽与信号连接
    send.sendmsg.connect(slot.get)
    # send 调用run函数触发信号
    send.run()
    # 槽与信号断开
    send.sendmsg.disconnect(slot.get)

    send.run()
