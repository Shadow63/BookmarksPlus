from PyQt5.QtWidgets import *
import sys


class CreateBookspace(QWidget):
    def __init__(self):
        super(CreateBookspace, self).__init__()
        layout = QVBoxLayout()
        name = QLineEdit()

        layout.addWidget(name)
        layout.addWidget(QPushButton('Top'))
        layout.addWidget(QPushButton('Bottom'))
        self.setLayout(layout)
