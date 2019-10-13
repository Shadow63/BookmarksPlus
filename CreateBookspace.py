import sys
from Bookspace import BookspacesData
from PyQt5.QtWidgets import *

import AddLinks

linksArray = []
usernameArray = []
passwordArray = []
focusedArray = []
nextArray = []
randomVar = 8
radioBrowser = ''

class CreateBookspace(QWidget):
    # Main Window
    def __init__(self, parentWindow):
        super().__init__()
        self.initui()
        self.parentWindow = parentWindow

    def initui(self):
        self.create_add_links_windows = []
        self.bowser = "Chrome"
        main_layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QGridLayout()

        # Naming the Bookspace
        fname = QLabel()
        fname.setText("Name of this Bookspace: ")
        self.name = QLineEdit()

        # Sets the layout
        layout2.addWidget(fname)
        layout2.addWidget(self.name)

        self.radiobutton1 = QRadioButton("Firefox")
        self.radiobutton1.toggled.connect(self.onClicked)
        layout3.addWidget(self.radiobutton1, 0, 0)

        self.radiobutton2 = QRadioButton("Chrome")
        self.radiobutton2.setChecked(True)
        self.radiobutton2.toggled.connect(self.onClicked)
        layout3.addWidget(self.radiobutton2, 0, 1)

        self.radiobutton3 = QRadioButton("Safari")
        self.radiobutton3.toggled.connect(self.onClicked)
        layout3.addWidget(self.radiobutton3, 0, 2)

        main_layout.addLayout(layout2)
        main_layout.addLayout(layout3)
        create = QPushButton('Create')
        main_layout.addWidget(create)
        create.clicked.connect(self.get_name_button)
        create.clicked.connect(resetLink)
        create.clicked.connect(self.close)

        links = QPushButton('Add a Link')
        main_layout.addWidget(links)
        links.clicked.connect(self.createAddLinksWindow)

        self.setLayout(main_layout)

    # Gets the name of the Bookspace
    def get_name_button(self):
        BookspacesData.add_bookspace(self.name.text(), linksArray, usernameArray, passwordArray, focusedArray, nextArray, self.bowser)
        self.parentWindow.addBookspaces(self.parentWindow.listWidget)
        return self.name.text()

    def createAddLinksWindow(self):
        create_add_links_window = AddLinks.AddLinks()
        create_add_links_window.show()
        self.create_add_links_windows.append(create_add_links_window)
#
    def onClicked(self):
        btn = self.sender()
        print(btn.text())
        self.bowser = btn.text()

def addLink(link):
    linksArray.append(link)

def addUsername(username):
    usernameArray.append(username)

def addPassword(password):
    passwordArray.append(password)

def addFocused(focus):
    focusedArray.append(focus)

def addNext(next):
    nextArray.append(next)

# Resets the array for each bookspace
def resetLink():
    while(len(linksArray) != 0):
        linksArray.pop()
        usernameArray.pop()
        passwordArray.pop()
        focusedArray.pop()
        nextArray.pop()

def run():
    app = QApplication(sys.argv)
    ex = CreateBookspace()
    ex.show()
    sys.exit(app.exec_())

