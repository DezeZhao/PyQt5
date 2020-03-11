# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 11:46
# @Software: PyCharm
# @File    : MultiWindows.py
# @Author  : DezeZhao

"""
多窗口交互：不使用信号与槽
win1里点击button 显示win2  win2关闭之后数据返回给win1
强耦合：在win1中访问win2的控件直接获取数据
win1 win2强关联在一起
要降低耦合  则需要使用信号与槽机制
"""

import sys

from PyQt5.QtWidgets import *

from DateDialog import DateDialog


class MultiWindows(QWidget):
    def __init__(self):
        super(MultiWindows, self).__init__()
        self.setWindowTitle('多窗口交互 不使用信号和槽')

        self.lineEdit = QLineEdit()
        self.lineEdit.setReadOnly(True)
        self.button1 = QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.onButton1Clicked)

        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.onButton2Clicked)

        grid = QGridLayout()
        grid.addWidget(self.lineEdit)
        grid.addWidget(self.button1)
        grid.addWidget(self.button2)

        self.setLayout(grid)

    # 访问控件
    def onButton1Clicked(self):
        dialog = DateDialog(self)
        result = dialog.exec()
        date = dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        dialog.destroy()

    # 访问静态方法  但也会访问到控件
    def onButton2Clicked(self):
        date, time, result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        if result == QDialog.Accepted:
            print('点击确定按钮')
        else:
            print('点击取消按钮')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MultiWindows()
    main.show()
    sys.exit(app.exec_())
