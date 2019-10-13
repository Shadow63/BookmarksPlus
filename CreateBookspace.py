import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *

import AddLinks


class CreateBookspace(QWidget):
    # Main Window
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.createAddLinksWindows = []
        self.links = []
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

        links = QPushButton('Add a Link')
        main_layout.addWidget(links)
        links.clicked.connect(self.createAddLinksWindow)

        self.setLayout(main_layout)

    # Gets the name of the Bookspace
    def get_name_button(self):
        print(self.links[0])
        return self.name.text()

    def createAddLinksWindow(self):
        create_add_links_window = AddLinks.AddLinks()
        create_add_links_window.show()
        self.links.append(create_add_links_window.get_name_button())
        self.createAddLinksWindows.append(create_add_links_window)


def run():
    app = QApplication(sys.argv)
    ex = CreateBookspace()
    ex.show()
    sys.exit(app.exec_())


