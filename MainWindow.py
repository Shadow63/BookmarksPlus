# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import CreateBookspace



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.createBookspaceWindows = []

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addBookspaceButton = QtWidgets.QPushButton(self.centralwidget)
        self.addBookspaceButton.setGeometry(QtCore.QRect(290, 390, 191, 61))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.addBookspaceButton.setFont(font)
        self.addBookspaceButton.setIconSize(QtCore.QSize(16, 16))

        self.addBookspaceButton.setObjectName("addBookspaceButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFILE = QtWidgets.QMenu(self.menubar)
        self.menuFILE.setObjectName("menuFILE")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNew_Bookspace = QtWidgets.QAction(MainWindow)
        self.actionNew_Bookspace.setObjectName("actionNew_Bookspace")
        self.menuFILE.addAction(self.actionNew_Bookspace)
        self.menubar.addAction(self.menuFILE.menuAction())

        self.addBookspaceButton.clicked.connect(self.createNewBookspaceWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addBookspaceButton.setText(_translate("MainWindow", "Add Bookspace"))
        self.menuFILE.setTitle(_translate("MainWindow", "File"))
        self.actionNew_Bookspace.setText(_translate("MainWindow", "New Bookspace"))
        self.actionNew_Bookspace.setStatusTip(_translate("MainWindow", "Create a new bookspace"))

    def createNewBookspaceWindow(self):
        createBookspaceWindow = CreateBookspace.CreateBookspace()
        createBookspaceWindow.show()
        CreateBookspace.resetLink()
        self.createBookspaceWindows.append(createBookspaceWindow)




def run():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

run()
