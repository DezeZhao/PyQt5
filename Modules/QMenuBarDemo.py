# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 13:32
# @Software: PyCharm
# @File    : QMenuBarDemo.py
# @Author  : DezeZhao
"""
创建和使用菜单

"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QMenuBarDemo(QMainWindow):
    def __init__(self):
        super(QMenuBarDemo, self).__init__()
        self.setWindowTitle('菜单栏演示')
        self.resize(500, 500)
        bar = self.menuBar()# 获取菜单栏

        file = bar.addMenu('文件')

        new = QAction('新建',self)
        file.addAction(new)
        save = QAction('保存',self)
        # 快捷键
        save.setShortcut('Ctrl + S')
        file.addAction(save)
        # 为动作QAction添加槽函数
        save.triggered.connect(self.process)
        quit = QAction('退出', self)
        file.addAction(quit)

        edit = bar.addMenu('Edit')
        edit.addAction('copy')
        edit.addAction('paste')


    def process(self):
        print(self.sender().text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMenuBarDemo()
    main.show()
    sys.exit(app.exec_())
