# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 13:47
# @Software: PyCharm
# @File    : QToolBarDemo.py
# @Author  : DezeZhao
"""
创建和使用工具栏
工具栏默认按钮悬停提示及工具栏按钮的显示状态
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QToolBarDemo(QMainWindow):
    def __init__(self):
        super(QToolBarDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('工具栏演示')
        self.resize(500,500)

        tb1 = self.addToolBar('File')
        new = QAction(QIcon('../assets/icons/new.png'),'new',self)
        tb1.addAction(new)
        open = QAction(QIcon('../assets/icons/open.png'),'open',self)
        tb1.addAction(open)
        save = QAction(QIcon('../assets/icons/save.png'),'save',self)
        tb1.addAction(save)

        # tb1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # tb1.setToolButtonStyle(Qt.ToolButtonIconOnly)
        # tb1.setToolButtonStyle(Qt.ToolButtonTextOnly)
        # tb1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        tb2 = self.addToolBar('File1')
        new1 = QAction(QIcon('../assets/icons/new.png'),'new',self)
        tb2.addAction(new1)

        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        tb1.actionTriggered.connect(self.toolBarPressed)
        tb2.actionTriggered.connect(self.toolBarPressed)

    def toolBarPressed(self,a):
        print(a.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QToolBarDemo()
    main.show()
    sys.exit(app.exec_())
