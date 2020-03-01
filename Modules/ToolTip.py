# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 13:02
# @Software: PyCharm
# @File    : ToolTip.py
# @Author  : DezeZhao
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QToolTip, QWidget, QApplication, QHBoxLayout, QPushButton, QMainWindow


class TooltipForm(QMainWindow):
    def __init__(self):
        super(TooltipForm, self).__init__()
        self.initUI()
        self.button = QPushButton('我的按钮')
        self.button.setToolTip('this is a button')

        # 垂直布局
        layout = QHBoxLayout()
        layout.addWidget(self.button)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    def initUI(self):
        QToolTip.setFont(QFont('SimSun', 12))
        self.setToolTip("this is a QWidget")
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('设置控件提示信息')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('../assets/icons/download.png'))#  为当前应用的所有窗口设置图标
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())
