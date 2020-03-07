# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 21:40
# @Software: PyCharm
# @File    : QInputDialogDemo.py
# @Author  : DezeZhao

"""
QInputDialog 输入对话框
QInputDialog.getItem
QInputDialog.getText
QInputDialog.getInt
"""
import sys

from PyQt5.QtWidgets import *


class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('输入对话框演示')
        self.resize(400, 200)

        layout = QFormLayout()
        self.button1 = QPushButton('获取列表选项')
        self.button1.clicked.connect(self.getItem)
        self.LineEdit1 = QLineEdit()
        layout.addRow(self.button1, self.LineEdit1)

        self.button2 = QPushButton('获取字符串')
        self.button2.clicked.connect(self.getText)
        self.LineEdit2 = QLineEdit()
        layout.addRow(self.button2, self.LineEdit2)

        self.button3 = QPushButton('获取整数')
        self.button3.clicked.connect(self.getInt)
        self.LineEdit3 = QLineEdit()
        layout.addRow(self.button3, self.LineEdit3)

        self.setLayout(layout)

    def getItem(self):
        items = ('C', 'C++', 'Python', 'Java', 'Go')
        items, ok = QInputDialog.getItem(self, '请选择编程语言', '语言列表', items)
        if ok and items:
            self.LineEdit1.setText(items)

    def getText(self):
        text, ok = QInputDialog.getText(self, '文本输入框', '输入姓名')
        if ok and text:
            self.LineEdit2.setText(text)

    def getInt(self):
        num, ok = QInputDialog.getInt(self, '整数输入框', '请输入整数')
        if ok and num:
            self.LineEdit3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())

