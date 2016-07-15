# -*- coding: utf-8 -*-

"""
QColorDialog
"""

import sys
from PyQt5.QtWidgets import (QSizePolicy, QLabel, QFontDialog, QWidget, QPushButton, QFrame, QLineEdit, QColorDialog,
                             QApplication, QHBoxLayout, QVBoxLayout, QInputDialog, QAction, QFileDialog, QTextEdit)
from PyQt5.QtGui import QColor, QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0) # black

        vbox = QVBoxLayout()
        self.btn = QPushButton('Color', self)
        self.btn.clicked.connect(self.showDialog)
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        vbox.addWidget(self.btn)
        vbox.addWidget(self.frm)

        hbox = QHBoxLayout()
        self.ibtn = QPushButton('Input', self)
        self.ibtn.clicked.connect(self.showInputDialog)
        self.le = QLineEdit('?', self)
        hbox.addWidget(self.ibtn)
        hbox.addWidget(self.le)

        hbox2 = QHBoxLayout()
        self.fbtn = QPushButton('Font', self)
        self.fbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        hbox2.addWidget(self.fbtn)
        self.fbtn.clicked.connect(self.fontDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        hbox2.addWidget(self.lbl)

        #self.textEdit = QTextEdit()
        #self.setCentralWidget(self.textEdit)
        #self.statusBar()

        #openFile = QAction(QIcon('open.png'), 'Open', self)
        #openFile.setShortcut('Ctrl+O')
        #openFile.setStatusTip('Open new File')
        #openFile.triggered.connect(self.openFileDialog)

        #menubar = self.menuBar()
        #fileMenu = menubar.addMenu('&File')
        #fileMenu.addAction(openFile)

        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        #vbox.addWidget(self.textEdit)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())

    def showInputDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:') #return str and bool value
        if ok:
            self.le.setText(str(text))

    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

    #def openFileDialog(self):
        #fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        #if fname[0]:
        #    f = open(fname[0], 'r')

        #    with f:
        #       data = f.read()
        #       self.textEdit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())