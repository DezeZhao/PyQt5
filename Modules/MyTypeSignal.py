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
    sendmsg = pyqtSignal(object)  # 传递的参数的类型为对象 且传递的参数的个数为1个
    # 发送3个参数信号(object)
    sendmsg1 = pyqtSignal(str, int, int)  # 传递一个字符串 2个int
    # sendmsg1 = pyqtSignal(object, object, object)# 也可 表示传递3个对象 类型不确定


    def run1(self):
        self.sendmsg1.emit('hello', 3, 4)

    def run(self):
        # 触发信号
        self.sendmsg.emit('hello pyqt5')


class MySlot(QObject):
    def get(self, msg):
        print(msg)

    def get1(self,msg,a,b):
        print(msg)
        print(a)
        print(b)


if __name__ == '__main__':
    send = MyTypeSignal()
    slot = MySlot()
    # 槽与信号连接
    send.sendmsg.connect(slot.get)
    send.sendmsg1.connect(slot.get1)
    # send 调用run函数触发信号
    send.run()
    send.run1()
    # 槽与信号断开
    send.sendmsg.disconnect(slot.get)
    send.run()


