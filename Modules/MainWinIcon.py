# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 22:49
# @Software: PyCharm
# @File    : MainWinIcon.py
# @Author  : DezeZhao
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWinIcon(QMainWindow):
    def __init__(self):
        super(MainWinIcon, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 500)
        # 设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")
        # 设置窗口的图标
        self.setWindowIcon(QIcon('../assets/icons/download.png'))  # 只为当前窗口设置图标


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('../assets/icons/download.png'))#  为当前应用的所有窗口设置图标
    main = MainWinIcon()
    main.show()
    sys.exit(app.exec_())
