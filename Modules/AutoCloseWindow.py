# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 23:37
# @Software: PyCharm
# @File    : AutoCloseWindow.py
# @Author  : DezeZhao
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel('<font color=red size=140>Hello World 窗口将在3秒后关闭！</font>')
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)

    label.show()
    QTimer.singleShot(3000, app.quit)
    sys.exit(app.exec_())
