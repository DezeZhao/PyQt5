# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 16:12
# @Software: PyCharm
# @File    : QLineEditDemo.py
# @Author  : DezeZhao
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        e1 = QLineEdit()
        # 使用int校验器
        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        e1.setAlignment(Qt.AlignRight)
        e1.setFont(QFont('Courier New'))

        e2 = QLineEdit()
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        # 掩码校验
        e3 = QLineEdit()
        e3.setInputMask('99_9999_99999;#')

        e4 = QLineEdit()
        e4.textChanged.connect(self.textChanged)

        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)
        e5.editingFinished.connect(self.enterPress)

        e6 = QLineEdit()
        e6.setReadOnly(True)

        formLayout = QFormLayout()
        formLayout.addRow('int valid', e1)
        formLayout.addRow('double valid', e2)
        formLayout.addRow('InputMask', e3)
        formLayout.addRow('text changed', e4)
        formLayout.addRow('password', e5)
        formLayout.addRow('read only', e6)
        self.setLayout(formLayout)
        self.setWindowTitle('QLineEdit综合实验')

    def textChanged(self, text):
        print("文本改变,输入的内容是" + text)

    def enterPress(self):
        print('enter 键按下,输入完毕')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditDemo()
    main.show()
    sys.exit(app.exec_())