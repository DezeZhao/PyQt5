# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 12:52
# @Software: PyCharm
# @File    : QDateTimeEdit1.py
# @Author  : DezeZhao

"""
不同风格日期设置
QDateTimeEdit

SIGNAL:
dateChanged
timeChanged
datetimeChanged
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QDateTimeEdit1(QWidget):
    def __init__(self):
        super(QDateTimeEdit1, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(350, 500)
        self.setWindowTitle('不同风格日期时间')

        layout = QVBoxLayout()

        dateTimeEdit1 = QDateTimeEdit()
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
        # 设置日期最大和最小值
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))

        self.dateTimeEdit=dateTimeEdit1

        dateTimeEdit2.setCalendarPopup(True)  # 上下箭头调整日期变为下拉

        #分别显示日期和时间
        dateEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())

        # 设置不同的日期时间显示格式
        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")

        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:ss")

        # 槽函数
        dateTimeEdit1.dateChanged.connect(self.onDateChange)
        dateTimeEdit1.timeChanged.connect(self.onTimeChange)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChange)

        layout.addWidget(dateTimeEdit1)
        layout.addWidget(dateTimeEdit2)
        layout.addWidget(dateEdit)
        layout.addWidget(timeEdit)
        self.btn=QPushButton('获取日期和时间')
        self.btn.clicked.connect(self.onButtonClick)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def onDateChange(self,date):
        print(date)

    def onTimeChange(self,time):
        print(time)

    def onDateTimeChange(self,datetime):
        print(datetime)

    def onButtonClick(self):
        dateTime= self.dateTimeEdit.dateTiem()
        print(dateTime)
        #最大/小日期(时间)
        print(self.dateTimeEdit.maximumDate())
        print(self.dateTimeEdit.maximumDateTime())
        print(self.dateTimeEdit.minimumDate())
        print(self.dateTimeEdit.minimumDateTime())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDateTimeEdit1()
    main.show()
    sys.exit(app.exec_())
