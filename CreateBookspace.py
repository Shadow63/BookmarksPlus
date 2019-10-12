from PyQt5.QtWidgets import *

app = QApplication([])


class CreateBookspace:

    window = QWidget()


    layout = QVBoxLayout()
    fname = QLabel()
    name = QLineEdit()

    #layout.addWidget(fname
    layout.addWidget(name)
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)
    window.show()

app.exec_()