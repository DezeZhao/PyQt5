# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 11:53
# @Software: PyCharm
# @File    : RightBottomBtn.py
# @Author  : DezeZhao
import sys

from PyQt5.QtWidgets import *


class RightBottomBtn(QWidget):
    def __init__(self):
        super(RightBottomBtn, self).__init__()
        self.setWindowTitle('让按钮永远在右下角')
        self.resize(500, 500)

        okbtn = QPushButton('ok')
        cancelbtn = QPushButton('cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okbtn)
        hbox.addWidget(cancelbtn)
        # hbox.addStretch(1) ## 此时两个按钮在中间

        vbox = QVBoxLayout()
        btn1 = QPushButton('按钮1')
        btn2 = QPushButton('按钮2')
        btn3 = QPushButton('按钮3')

        # vbox.addStretch(1)  # 三个按钮从下面开始排列
        vbox.addStretch(0)  # 三个按钮从上面开始排列
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addStretch(1)  # 从下面开始排
        vbox.addLayout(hbox)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = RightBottomBtn()
    main.show()
    sys.exit(app.exec_())
