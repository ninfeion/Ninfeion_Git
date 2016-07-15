# -*- utf-8 -*-

"""
THIS EXAMPLE CREATE A STATUSBAR, A MENUBAR.
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QAction
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready') # first time calling method statusBar of class QMainWindow will create a status bar

        exitAction = QAction(QIcon('pyqt5_demo6_exit_pic.png'), '&Exit', self) #
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        openAction = QAction(QIcon('pyqt5_demo6_exit_pic.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open file')
        #openAction.triggered.connect()

        optionAction = QAction(QIcon('pyqt5_demo6_exit_pic.png'), '&Option', self)
        #optionAction.setShortcut('Ctrl+O')
        optionAction.setStatusTip('Set up software option')

        self.toolbar = self.addToolBar('Exit') # add a tool bar
        self.toolbar.addAction(exitAction)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File') # add first level choice
        editMenu = menubar.addMenu('&Menu')

        fileMenu.addAction(openAction) # add second level choice of first level choice
        fileMenu.addAction(exitAction)

        editMenu.addAction(optionAction)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar and Menubar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())