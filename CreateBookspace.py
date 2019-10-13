import sys
from Bookspace import BookspacesData
from PyQt5.QtWidgets import *

import AddLinks

linksArray = []
usernameArray = []
passwordArray = []
focusedArray = []
nextArray = []

class CreateBookspace(QWidget):
    # Main Window
    def __init__(self, parentWindow):
        super().__init__()
        self.initui()
        self.parentWindow = parentWindow

    def initui(self):
        self.create_add_links_windows = []
        main_layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()

        # Naming the Bookspace
        fname = QLabel()
        fname.setText("Name of this Bookspace: ")
        self.name = QLineEdit()

        # Sets the layout
        layout2.addWidget(fname)
        layout2.addWidget(self.name)

        main_layout.addLayout(layout2)
        create = QPushButton('Create')
        main_layout.addWidget(create)
        create.clicked.connect(self.get_name_button)
        create.clicked.connect(self.close)

        links = QPushButton('Add a Link')
        main_layout.addWidget(links)
        links.clicked.connect(self.createAddLinksWindow)

        self.setLayout(main_layout)

    # Gets the name of the Bookspace
    def get_name_button(self):
        BookspacesData.add_bookspace(self.name.text(), linksArray, usernameArray, passwordArray, focusedArray, nextArray)
        self.parentWindow.addBookspaces(self.parentWindow.listWidget)
        return self.name.text()

    def createAddLinksWindow(self):
        create_add_links_window = AddLinks.AddLinks()
        create_add_links_window.show()
        # self.links.append(create_add_links_window.get_name_button())
        self.create_add_links_windows.append(create_add_links_window)

        # print(self.links)


def addLink(link):
    linksArray.append(link)
    print(linksArray)

def addUsername(username):
    usernameArray.append(username)
    print(usernameArray)

def addPassword(password):
    passwordArray.append(password)
    print(passwordArray)

def addFocused(focus):
    focusedArray.append(focus)
    print(focusedArray)

def addNext(next):
    nextArray.append(next)
    print(nextArray)

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


