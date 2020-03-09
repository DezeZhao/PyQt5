# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 10:44
# @Software: PyCharm
# @File    : ListWidget.py
# @Author  : DezeZhao
"""
SIGNAL:
itemClicked
"""
import sys

from PyQt5.QtWidgets import *


class ListWidget(QMainWindow):
    def __init__(self):
        super(ListWidget, self).__init__()
        self.setWindowTitle('扩展的列表控件')
        self.listwidget = QListWidget()
        self.listwidget.resize(300, 120)
        self.listwidget.addItem('item1')
        self.listwidget.addItem('item2')
        self.listwidget.addItems(['item3', 'item4'])
        self.listwidget.addItem('item5')
        self.listwidget.setWindowTitle('demo')

        self.listwidget.itemClicked.connect(self.clicked)

        self.setCentralWidget(self.listwidget)

    def clicked(self, index):
        QMessageBox.information(self, 'QListWidget', '您选择了' + self.listwidget.item(self.listwidget.row(index)).text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListWidget()
    main.show()
    sys.exit(app.exec_())
