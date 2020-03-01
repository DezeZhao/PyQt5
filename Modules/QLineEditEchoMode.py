# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 15:17
# @Software: PyCharm
# @File    : QLineEditEchoMode.py
# @Author  : DezeZhao
"""
QLineEdit
输入单行文本
EchoMode：回显模式

Normal、NoEcho
Password、PasswordEchoEdit

"""
import sys

from PyQt5.QtWidgets import *

from Modules.QuitApplication import QuitApplication


class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout = QFormLayout()
        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow('Normal', normalLineEdit)
        formLayout.addRow('NoEcho', noEchoLineEdit)
        formLayout.addRow('Password', passwordLineEdit)
        formLayout.addRow('PasswordEchoEdit', passwordEchoOnEditLineEdit)

        # placeholdertext
        normalLineEdit.setPlaceholderText('Normal')
        noEchoLineEdit.setPlaceholderText('NoEcho')
        passwordLineEdit.setPlaceholderText('Password')
        passwordEchoOnEditLineEdit.setPlaceholderText('PasswordEchoEdit')

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())
