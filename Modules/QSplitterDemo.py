# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 22:25
# @Software: PyCharm
# @File    : QSplitterDemo.py
# @Author  : DezeZhao
"""
拖动控件之间的边界QSplitter
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QSplitterDemo(QWidget):
    def __init__(self):
        super(QSplitterDemo, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QVBoxLayout(self)

        self.setWindowTitle('QSplitter演示')

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        textEdit = QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textEdit)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)

        self.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSplitterDemo()
    main.show()
    sys.exit(app.exec_())
