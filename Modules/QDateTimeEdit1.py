# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 12:52
# @Software: PyCharm
# @File    : QDateTimeEdit1.py
# @Author  : DezeZhao

"""
不同风格日期设置
QDateTimeEdit
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QDateTimeEdit1(QWidget):
    def __init__(self):
        super(QDateTimeEdit1, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('不同风格日期')

        layout = QVBoxLayout()
        dateTimeEdit1=QDateTimeEdit()
        dateTimeEdit2=QDateTimeEdit()

        dateEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())

        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")

        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:ss")

        layout.addWidget(dateTimeEdit1)
        layout.addWidget(dateTimeEdit2)
        layout.addWidget(dateEdit)
        layout.addWidget(timeEdit)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDateTimeEdit1()
    main.show()
    sys.exit(app.exec_())

