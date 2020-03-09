# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 23:15
# @Software: PyCharm
# @File    : MultiSignals.py
# @Author  : DezeZhao
"""
为一个类定义多个信号  及 重载的信号触发和槽函数连接的方式
"""
from PyQt5.QtCore import *


class MultiSignals(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int)
    signal3 = pyqtSignal(int, str)
    signal4 = pyqtSignal(list)
    signal5 = pyqtSignal(dict)
    # 声明一个重载版本的信号，也就是槽函数可以是int&str 也可以是只有str 参数
    signal6 = pyqtSignal([int, str], [str])

    def __init__(self):
        super(MultiSignals, self).__init__()
        self.signal1.connect(self.singalCall1)
        self.signal2.connect(self.singalCall2)
        self.signal3.connect(self.singalCall3)
        self.signal4.connect(self.singalCall4)
        self.signal5.connect(self.singalCall5)
        self.signal6[int, str].connect(self.singalCall6)# 重载形式的信号
        self.signal6[str].connect(self.singalCall6Overload)# 重载形式的信号

        # 触发信号 通过emit来传递参数
        self.signal1.emit()
        self.signal2.emit(10)
        self.signal3.emit(1,'hello world')
        self.signal4.emit([1,2,3,4,5])
        self.signal5.emit({'name':'Zhaodeze','age':21})
        self.signal6[int,str].emit(100,'myString')
        self.signal6[str].emit('Mystring')

    # 槽函数 接收信号触发emit时传递的参数
    def singalCall1(self):
        print("signal1 emit")

    def singalCall2(self, val):
        print("signal2 emit ", val)

    def singalCall3(self, val, text):
        print("signal3 emit ", val, text)

    def singalCall4(self, val):
        print("signal4 emit ", val)

    def singalCall5(self, val):
        print("signal5 emit ", val)

    def singalCall6(self, val, text):
        print("signal6 emit ", val, text)

    def singalCall6Overload(self, val):
        print("signal6 emit ", val)

if __name__ == '__main__':
        multisignals = MultiSignals()