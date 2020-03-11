# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 11:51
# @Software: PyCharm
# @File    : DateDialog.py
# @Author  : DezeZhao

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DateDialog(QDialog):
    def __init__(self, parent=None):  # 此处必须有parent？？？？
        super(DateDialog, self).__init__(parent)
        self.setWindowTitle('DateDialog')

        layout = QVBoxLayout(self)
        self.datetime = QDateTimeEdit()
        # self.datetime.setReadOnly(True)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.datetime)

        button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        button.accepted.connect(self.accept)
        button.rejected.connect(self.reject)

        layout.addWidget(button)

    def dateTime(self):
        return self.datetime.dateTime()

    @staticmethod
    def getDateTime(parent=None):
        dialog = DateDialog(parent)
        result = dialog.exec()
        date = dialog.dateTime()
        return date.date(), date.time(), result == QDialog.Accepted
