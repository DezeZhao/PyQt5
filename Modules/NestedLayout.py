# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 16:25
# @Software: PyCharm
# @File    : NestedLayout.py
# @Author  : DezeZhao
"""
嵌套布局
两种方案实现
1. 用一个QWidget来承载一个全局布局QLayout,在全局QLayout中addLayout，最后setLayout即可
2. 用每个QWidget来承载QLayout,然后在全局QLayout中addWidget，最后setLayout即可
"""
import sys

from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("嵌套布局示例")
        # 全局控件用于承载全局布局
        wwg = QWidget(self)
        # 全局布局 水平（设置4个hwg ,vwg ...时用）
        wlayout1 = QHBoxLayout()
        # 全局布局 水平 （addLayout时用）
        wlayout2 = QHBoxLayout(wwg)

        # 局部布局
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        glayout = QGridLayout()
        formlayout = QFormLayout()

        # 为局部布局添加控件
        hlayout.addWidget(QPushButton(str(1)))
        hlayout.addWidget(QPushButton(str(2)))
        vlayout.addWidget(QPushButton(str(3)))
        vlayout.addWidget(QPushButton(str(4)))
        glayout.addWidget(QPushButton(str(5)), 0, 0)
        glayout.addWidget(QPushButton(str(6)), 0, 1)
        glayout.addWidget(QPushButton(str(7)), 1, 0)
        glayout.addWidget(QPushButton(str(8)), 1, 1)
        formlayout.addWidget(QPushButton(str(9)))
        formlayout.addWidget(QPushButton(str(10)))
        formlayout.addWidget(QPushButton(str(11)))
        formlayout.addWidget(QPushButton(str(12)))
        """
        # 四个QWidget控件
        hwg = QWidget()
        vwg = QWidget()
        gwg = QWidget()
        fwg = QWidget()

        # 使用四个控件进行设备局部布局
        hwg.setLayout(hlayout)
        vwg.setLayout(vlayout)
        gwg.setLayout(glayout)
        fwg.setLayout(formlayout)
        # 添加到全局布局
        wlayout1.addWidget(hwg)
        wlayout1.addWidget(vwg)
        wlayout1.addWidget(gwg)
        wlayout1.addWidget(fwg)
        
        self.setLayout(wlayout1)
        """
        wlayout2.addLayout(hlayout)
        wlayout2.addLayout(vlayout)
        wlayout2.addLayout(glayout)
        wlayout2.addLayout(formlayout)

        # 将窗口本身设置为全局布局
        self.setLayout(wlayout2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
