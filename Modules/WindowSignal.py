# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 23:35
# @Software: PyCharm
# @File    : WindowSignal.py
# @Author  : DezeZhao

"""
为窗口添加信号
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class WindowSignal(QWidget):
    button = pyqtSignal()

    def __init__(self):
        super(WindowSignal, self).__init__()
        self.resize(300, 100)
        btn = QPushButton('关闭窗口', self)
        # 按钮btn触发 button信号
        btn.clicked.connect(self.btn_clicked)
        # button 信号和槽函数连接 执行槽函数
        self.button.connect(self.btn_close)

    def btn_clicked(self):
        self.button.emit()

    def btn_close(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WindowSignal()
    main.show()
    sys.exit(app.exec_())
