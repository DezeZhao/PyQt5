# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 15:40
# @Software: PyCharm
# @File    : QLineEditValidator.py
# @Author  : DezeZhao
"""
QLineEdit 控件的输入
限制输入整数，浮点数，或满足一定条件
"""
import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QApplication


class QLineEDitValidator(QWidget):
    def __init__(self):
        super(QLineEDitValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')

        formLayout = QFormLayout()
        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        regLineEdit = QLineEdit()

        formLayout.addRow('整数', intLineEdit)
        formLayout.addRow('浮点数', doubleLineEdit)
        formLayout.addRow('正则表达式', regLineEdit)

        intLineEdit.setPlaceholderText('整型数字')
        doubleLineEdit.setPlaceholderText('浮点数')
        regLineEdit.setPlaceholderText('正则表达式')

        intValidator = QIntValidator()
        intValidator.setRange(0, 1000)

        doubleValidator = QDoubleValidator()
        doubleValidator.setRange(-100, 100)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)  # 小数精度

        reg = QRegExp(r"[a-zA-Z0-9]+$")
        regValidator = QRegExpValidator(self)
        regValidator.setRegExp(reg)

        # 设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        regLineEdit.setValidator(regValidator)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEDitValidator()
    main.show()
    sys.exit(app.exec_())
