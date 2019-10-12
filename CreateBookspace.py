import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *

#app = QApplication([])

def get_name(something):
    print(something.text())

class CreateBookspace(QWidget):
    # Main Window
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        layout = QVBoxLayout()
        layout2 = QHBoxLayout()

        # Setting the name of the Bookspace
        fname = QLabel()
        fname.setText("Name of this Bookspace: ")
        name = QLineEdit()

        layout2.addWidget(fname)
        layout2.addWidget(name)


        # Some Buttons
        layout.addLayout(layout2)
        create = QPushButton('Create')
        word = name.text()

        layout.addWidget(create)
        create.clicked.connect(lambda: self.handleButton())
        layout.addWidget(QPushButton('Bottom'))
        self.setLayout(layout)

    def handleButton(self):
        print(self.get_name)

    def get_name(self):
        print(self.name.text)
        return self.name.text()


def run():
    app = QApplication(sys.argv)
    ex = CreateBookspace()
    ex.show()
    sys.exit(app.exec_())

run()
