# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 17:46
# @Software: PyCharm
# @File    : NewDateDialog.py
# @Author  : DezeZhao

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class NewDateDialog(QDialog):
    signalOneArg = pyqtSignal(str)  # 自定义信号

    def __init__(self, parent=None):
        super(NewDateDialog, self).__init__(parent)

        self.resize(400, 200)

        self.setWindowTitle('子窗口，用于发信号')

        layout = QVBoxLayout(self)
        self.datetime_inner = QDateTimeEdit()
        self.datetime_emit = QDateTimeEdit()
        self.datetime_inner.setCalendarPopup(True)
        self.datetime_emit.setCalendarPopup(True)
        self.datetime_emit.setDateTime(QDateTime.currentDateTime())
        self.datetime_inner.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.datetime_inner)
        layout.addWidget(self.datetime_emit)

        button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
                                  Qt.Horizontal, self)
        button.accepted.connect(self.accept)
        button.rejected.connect(self.reject)

        layout.addWidget(button)

        # 当日期时间改变的时候触发发送信号的槽函数
        # 从而将子窗口的信号释放
        # 此处还是调用内置的信号 dateTimeChanged
        self.datetime_emit.dateTimeChanged.connect(self.emit_signal)

    # 自定义信号发送参数给父窗口
    def emit_signal(self):
        date_Str = self.datetime_emit.dateTime().toString()
        self.signalOneArg.emit(date_Str)  # 释放信号
