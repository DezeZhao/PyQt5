# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 12:42
# @Software: PyCharm
# @File    : MyCalendar.py
# @Author  : DezeZhao
"""
日历kongjian
QCalendarWidget
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUI()

    def initUI(self):
        self.cal = QCalendarWidget(self)  # 直接放在窗口  绝对布局
        self.cal.setMinimumDate(QDate(1988, 1, 1))
        self.cal.setMaximumDate(QDate(2050, 1, 1))

        self.cal.setGridVisible(True)
        self.cal.move(20, 20)

        self.cal.clicked.connect(self.showDate)
        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString("yyyy-MM-dd dddd"))
        self.label.move(20, 400)
        self.setWindowTitle('日历控件')
        self.resize(500, 500)

    def showDate(self, date):
        self.label.setText(date.toString("yyyy-MM-dd dddd"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyCalendar()
    main.show()
    sys.exit(app.exec_())
