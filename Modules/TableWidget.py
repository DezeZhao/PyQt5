# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 10:58
# @Software: PyCharm
# @File    : TableWidget.py
# @Author  : DezeZhao

import sys

from PyQt5.QtWidgets import *


class TableWidget(QWidget):
    def __init__(self):
        super(TableWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableWidget演示')
        self.resize(500, 500)

        layout = QVBoxLayout()
        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)

        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['name', 'age', 'province'])
        nameItem = QTableWidgetItem('小明')
        tablewidget.setItem(0, 0, nameItem)

        ageItem = QTableWidgetItem('24')
        tablewidget.setItem(0, 1, ageItem)

        jgItem = QTableWidgetItem('北京')
        tablewidget.setItem(0, 2, jgItem)
        # 设为不能编辑
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设为整行选中
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 使得内容自动适应行列宽高
        tablewidget.resizeColumnsToContents()
        tablewidget.resizeRowsToContents()


        # 隐藏水平列标题
        tablewidget.horizontalHeader().setVisible(False)
        # 隐藏垂直行标题
        tablewidget.verticalHeader().setVisible(False)
        # 为每行添加头标签
        tablewidget.setVerticalHeaderLabels(['a','b'])
        # 隐藏表格线
        tablewidget.setShowGrid(False)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableWidget()
    main.show()
    sys.exit(app.exec_())
