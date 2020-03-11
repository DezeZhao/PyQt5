# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 23:50
# @Software: PyCharm
# @File    : lambdaSlotArg.py
# @Author  : DezeZhao
"""
lambda表达式为槽函数传参

Lambda表达式 匿名函数 也就是没名字的函数
fun = lambda :print('shdshc')

fun()

fun1 = lambda x,y:print(x,y)
fun1(2,3)
"""
import sys

from PyQt5.QtWidgets import *


class lambdaSlotArg(QWidget):
    def __init__(self):
        super(lambdaSlotArg, self).__init__()
        self.setWindowTitle('lambda表达式传参')

        btn1 = QPushButton('按钮1')
        btn2 = QPushButton('按钮2')

        # btn1.clicked.connect(self.onButton1)  # 这样连接是不会传参数的
        btn1.clicked.connect(lambda: self.onButton1(10, 20))
        btn2.clicked.connect(lambda: self.onButton2(10, 20))
        layout = QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        self.setLayout(layout)  # 若继承自QWidget则直接用setLayout即可布局
        # 否则若继承自QMainWindow则需要先添加一个QWidget,再用setLayout布局，
        # 最后setCentralWidget(QWidget)即可布局
        # mainframe = QWidget()
        # mainframe.setLayout(layout)
        # self.setCentralWidget(mainframe)

    def onButton1(self, m, n):
        QMessageBox.information(self, '结果', str('m + n = ') + str(m + n))

    def onButton2(self, m, n):
        QMessageBox.information(self, '结果', str('m * n = ') + str(m * n))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = lambdaSlotArg()
    main.show()
    sys.exit(app.exec_())
