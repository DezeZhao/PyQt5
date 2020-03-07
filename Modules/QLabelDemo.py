# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 13:36
# @Software: PyCharm
# @File    : QLabelDemo.py
# @Author  : DezeZhao

'''
QLabel
setAlignment()
setIndent()
test()
setBuddy()
setText()
selectedText()
setWordWrap()
QLabel 常用的信号：
当鼠标划过label：linkHovered
当鼠标点击label：linkActivated
'''
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication


class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel()
        label2 = QLabel()
        label3 = QLabel()
        label4 = QLabel()

        label1.setText('这是一个文本标签')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.darkGray)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用GUI</a>")

        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap('../assets/images/pythonlogo.png'))

        label4.setText("<a href='https://www.baidu.com'>欢迎使用百度</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接')

        VBox = QVBoxLayout()
        VBox.addWidget(label1)
        VBox.addWidget(label2)
        VBox.addWidget(label3)
        VBox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkActivated)

        self.setLayout(VBox)
        # self.resize(700,500)
        self.setWindowTitle('Qlabel 控件演示')

    def linkHovered(self):
        print('hover label2')

    def linkActivated(self):
        print('click label4')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())