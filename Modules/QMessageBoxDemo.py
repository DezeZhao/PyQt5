# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 18:12
# @Software: PyCharm
# @File    : QMessageBoxDemo.py
# @Author  : DezeZhao
"""
关于对话框
错误对话框
警告对话框
提示对话框
消息对话框

不同点：
显示对话框图标可能不一样
对话框显示的按钮时不一样的
"""
import sys

from PyQt5.QtWidgets import *


class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QMessageBox演示')
        self.resize(500, 400)

        layout = QVBoxLayout()
        self.btn1 = QPushButton()
        self.btn1.setText('显示关于对话框')
        self.btn1.clicked.connect(self.showDialog)
        layout.addWidget(self.btn1)

        self.btn2 = QPushButton('显示消息对话框')
        self.btn2.clicked.connect(self.showDialog)
        layout.addWidget(self.btn2)

        self.btn3 = QPushButton('显示警告对话框')
        self.btn3.clicked.connect(self.showDialog)
        layout.addWidget(self.btn3)

        self.btn4 = QPushButton('显示错误对话框')
        self.btn4.clicked.connect(self.showDialog)
        layout.addWidget(self.btn4)

        self.btn5 = QPushButton('显示提问对话框')
        self.btn5.clicked.connect(self.showDialog)
        layout.addWidget(self.btn5)

        self.setLayout(layout)

    def showDialog(self):
        text = self.sender().text()
        if text == '显示关于对话框':
            QMessageBox.about(self, '关于', '这是一个关于对话框')
        if text == '显示消息对话框':
            reply = QMessageBox.information(self, '消息', '这是一个消息对话框', QMessageBox.Yes | QMessageBox.No)
            print(reply == QMessageBox.Yes)
        if text == '显示警告对话框':
            QMessageBox.warning(self, '警告', '这是一个警告对话框', QMessageBox.No | QMessageBox.Yes)
        if text == '显示错误对话框':
            QMessageBox.critical(self, '错误', '这是一个错误对话框', QMessageBox.No | QMessageBox.Yes)
        if text == '显示提问对话框':
            QMessageBox.question(self,'提问','这是一个提问对话框',QMessageBox.No|QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.show()
    sys.exit(app.exec_())
