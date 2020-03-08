# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 23:18
# @Software: PyCharm
# @File    : showTime.py
# @Author  : DezeZhao
"""
动态显示当前时间---多线程并发完成任务
QTimer——完成周期性任务（定时器）
QThread
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class showTime(QWidget):
    def __init__(self):
        super(showTime, self).__init__()
        self.setWindowTitle('动态显示时间')
        self.resize(500, 500)

        self.label = QLabel('显示当前时间')
        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')

        layout = QGridLayout()
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime1)

        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)
        self.setLayout(layout)

    def showTime1(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label.setText(timeDisplay)

    def startTimer(self):
        self.timer.start()
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.endBtn.setEnabled(False)
        self.startBtn.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = showTime()
    main.show()
    sys.exit(app.exec_())
