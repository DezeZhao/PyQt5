# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 14:27
# @Software: PyCharm
# @File    : QStatusBarDemo.py
# @Author  : DezeZhao
"""
状态栏
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QStatusBarDemo(QMainWindow):
    def __init__(self):
        super(QStatusBarDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('状态栏演示')
        self.resize(500, 500)

        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('show')
        file.triggered.connect(self.process)

        self.statusBar = QStatusBar()
        self.setCentralWidget(QTextEdit())
        self.setStatusBar(self.statusBar)

    def process(self, q):
        if q.text() == 'show':
            self.statusBar.showMessage(q.text() + '菜单被点击了', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QStatusBarDemo()
    main.show()
    sys.exit(app.exec_())