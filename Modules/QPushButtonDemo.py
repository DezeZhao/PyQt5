# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 18:26
# @Software: PyCharm
# @File    : QPushButtonDemo.py
# @Author  : DezeZhao
"""
QPushButton
QToolButton
QRadioButton
QCheckBox
----QPushButton
主要方法有——
setCheckable()
# 设置按钮是否已经被选中，如果设置为true，
# 则表示按钮将保持自己的点击和释放状态
toggle()
# 按钮状态之间进行切换
setIcon()
# 设置图标
setEnabled(bool)
# False 时按钮点击不可用，将不会触发信号
isChecked()
# 返回按钮状态，True /False
setDefault()
#设置按钮的默认状态
setText()
text()
# 得到按钮的文本

"""
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton 演示')
        layout = QVBoxLayout()

        self.button1 = QPushButton('button1')
        self.button1.setText('first button')
        self.button1.setCheckable(True)
        self.button1.toggle()
        # lambda表达式传参
        self.button1.clicked.connect(self.buttonState)
        self.button1.clicked.connect(lambda: self.whichButton(self.button1))

        # 在文本前显示图像
        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('../assets/icons/download.png')))
        self.button2.clicked.connect(lambda: self.whichButton(self.button2))

        self.button3 = QPushButton('不可用的按钮')
        self.button3.setEnabled(False)

        self.button4 = QPushButton('默认按钮')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda: self.whichButton(self.button4))

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)

        self.setLayout(layout)

    def whichButton(self, btn):
        print('被点击的按钮是<' + btn.text() + '>')

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮1被选中')
        else:
            print('按钮1未被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())
