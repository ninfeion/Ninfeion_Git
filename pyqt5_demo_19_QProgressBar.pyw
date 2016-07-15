#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a QProgressBar widget.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar, QGridLayout,
                             QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #grid = QGridLayout()

        self.pbar = QProgressBar(self) # create a progressbar that default range cover 0~99
        self.pbar.setGeometry(30, 40, 200, 25)
        #grid.addWidget(self.pbar, 1, 0)
        self.pbar.setMaximum(1999)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        #grid.addWidget(self.btn, 2, 0)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer() # create a instance of timer
        self.step = 0

        #self.setLayout(grid)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):

        if self.step >= 2000:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())