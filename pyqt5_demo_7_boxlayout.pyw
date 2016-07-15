# -*- coding: utf-8 -*-

"""
BoxLayout:QHBoxLayout,QVBoxLayout
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1) # 增加拉伸因子 在添加按键之前 所以在按键的左边会有一个可伸缩空间 按键在窗口右边
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1) # 拉伸因子 空间在布局的上面
        vbox.addLayout(hbox) # addLayout -> Layout 水平布局放垂直布局里面

        self.setLayout(vbox) # 设置主窗口的布局

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())