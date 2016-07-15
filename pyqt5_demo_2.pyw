# -*- coding: utf-8 -*-

"""
An Expression Evaluator
"""

#__author__ = "Ninfeion"

from __future__ import division
import sys
from math import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time


class Form(QDialog):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)

        self.setLayout(layout)
        self.lineedit.setFocus()
        #PyQt4 Old Style signals and slots
        #self.connect(self.lineedit, pyqtSignal("returnPressed()"),
        #             self.updateUi)
        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = self.lineedit.text()
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append(
                    "<font color=red>%s is invalid!</font>" % text)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
