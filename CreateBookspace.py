from PyQt5.QtWidgets import *

app = QApplication([])


class CreateBookspace:
    # Main Window
    window = QWidget()
    layout = QVBoxLayout()

    # Setting the name of the Bookspace
    fname = QLabel()
    name = QLineEdit()

    layout.addWidget(fname)
    layout.addWidget(name)

    # Some Buttons
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)
    window.show()

    def run():
        app.exec_()

    run()