# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 10:25
# @Software: PyCharm
# @File    : TableView.py
# @Author  : DezeZhao
"""
需要创建tableview实例并且将两者相关联
数据源 model
MVC
model view controller
将后端的数据和前端页面的耦合度降到最低
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TableView(QWidget):
    def __init__(self):
        super(TableView, self).__init__()
        self.setWindowTitle('QTableView控件')
        self.resize(700,500)

        self.model = QStandardItemModel(4,3) # 4行3列
        self.model.setHorizontalHeaderLabels(['id','name','age'])
        self.tableview = QTableView()
        # 关联ATableview和数据model
        self.tableview.setModel(self.model)

        # 添加数据
        item1 = QStandardItem('10')
        item2 = QStandardItem('nvnj')
        item3 = QStandardItem('2000')

        self.model.setItem(0, 0, item1)
        self.model.setItem(0, 1, item2)
        self.model.setItem(0, 2, item3)

        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableView()
    main.show()
    sys.exit(app.exec_())
