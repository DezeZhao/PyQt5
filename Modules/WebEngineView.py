# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 23:44
# @Software: PyCharm
# @File    : WebEngineView.py
# @Author  : DezeZhao
"""
PyQt5和web的交互技术
同时使用python和web技术混合开发
同时使用python JavaScript html5 css3
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView, self).__init__()
        self.setWindowTitle('打开外部网页')
        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://www.jd.com'))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WebEngineView()
    main.show()
    sys.exit(app.exec_())
