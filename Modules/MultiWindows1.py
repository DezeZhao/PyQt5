# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 17:39
# @Software: PyCharm
# @File    : MultiWindows1.py
# @Author  : DezeZhao
"""
多窗口交互：信号与槽实现

如果A窗口与另一个B窗口交互 那么A尽量不要直接访问B窗口的控件
应该访问B中的信号 并指定与信号关联的槽函数

如果A直接访问B中的控件，一旦B窗口中的控件发生改变那么还要改变
A B的程序代码  否则  只需要修改B代码即可

"""
import sys

from PyQt5.QtWidgets import *

from NewDateDialog import NewDateDialog


class MultiWindows1(QWidget):
    def __init__(self):
        super(MultiWindows1, self).__init__()
        self.resize(600, 300)
        self.setWindowTitle('多窗口交互-使用信号与槽')

        self.open_btn = QPushButton('获取时间')

        self.lineEdit_inner = QLineEdit(self)
        self.lineEdit_emit = QLineEdit(self)

        self.open_btn.clicked.connect(self.openDialog)

        self.lineEdit_inner.setText('接受子窗口内置信号的时间')
        # self.lineEdit_inner.setReadOnly(True)
        self.lineEdit_emit.setText('接受子窗口自定义信号的时间')
        # self.lineEdit_emit.setReadOnly(True)
        grid = QGridLayout()
        grid.addWidget(self.lineEdit_inner)
        grid.addWidget(self.lineEdit_emit)
        grid.addWidget(self.open_btn)

        self.setLayout(grid)

    def openDialog(self):
        dialog = NewDateDialog(self)
        dialog.setModal(True)
        # 内置的信号来进行窗口间交互  此处是直接访问子窗口的控件datetime_inner
        dialog.datetime_inner.dateTimeChanged.connect(self.deal_inner_slot)

        # 自定义的信号来进行窗口交互  此处是访问子窗口的信号 signalOneArg
        # signalOneArg 触发时会传递一个参数 date 从而回传给与之关联的槽函数
        dialog.signalOneArg.connect(self.deal_emit_slot)
        dialog.show()

    def deal_inner_slot(self, date):
        self.lineEdit_inner.setText(date.toString())

    def deal_emit_slot(self, dateStr):
        self.lineEdit_emit.setText(dateStr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MultiWindows1()
    main.show()
    sys.exit(app.exec_())
