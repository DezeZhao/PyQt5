# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 23:30
# @Software: PyCharm
# @File    : AutoSignalSlot.py
# @Author  : DezeZhao
"""
自动连接槽和信号
自动绑定时槽函数的命名规则为 on_QObjectName_QSignalName
on_okBtn_clicked
on_cancelBtn_clicked
"""
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot, self).__init__()
        self.okBtn = QPushButton('ok')
        self.okBtn.setObjectName('okBtn')  # 为button设置名称  从而和槽函数绑定
        self.cancelBtn = QPushButton('cancel')
        self.cancelBtn.setObjectName('cancelBtn')
        layout = QHBoxLayout()
        layout.addWidget(self.okBtn)
        layout.addWidget(self.cancelBtn)
        self.setLayout(layout)
        QtCore.QMetaObject.connectSlotsByName(self)

    # 表示该函数是槽函数
    @QtCore.pyqtSlot()
    def on_okBtn_clicked(self):
        print('okBtn is clicked')

    # 表示该函数是槽函数
    @QtCore.pyqtSlot()
    def on_cancelBtn_clicked(self):
        print('cancelBtn is clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AutoSignalSlot()
    main.show()
    sys.exit(app.exec_())
