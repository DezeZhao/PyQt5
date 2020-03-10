# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 23:47
# @Software: PyCharm
# @File    : ThreadUpdate.py
# @Author  : DezeZhao

"""
多线程更新UI窗口数据
"""
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class BackendThread(QThread):  # 线程类
    update_date = pyqtSignal(str)  # 自定义信号对象

    def run(self):  # 线程执行函数  其实就是 释放信号 把数据传递给槽函数
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(currentTime)  # 把当前时间传递给槽函数
            time.sleep(1)


class ThreadUpdateUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('多线程更新UI数据')
        self.resize(400, 100)
        self.input = QLineEdit(self)
        self.input.setReadOnly(True)
        self.initUI()

    def initUI(self):
        self.backend = BackendThread()  # 实例化一个线程
        self.backend.update_date.connect(self.handleDisplay)  # 线程的信号和槽函数连接 触发信号时就执行槽函数
        self.backend.start()  # 线程开始 通过start函数间接调用run函数  不能直接调用run函数

    def handleDisplay(self, data):
        self.input.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ThreadUpdateUI()
    main.show()
    sys.exit(app.exec_())
