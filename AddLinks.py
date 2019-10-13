import sys
from PyQt5.QtWidgets import *
import CreateBookspace

class AddLinks(QWidget):
    # Main Window
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        main_layout = QVBoxLayout()
        layout2 = QHBoxLayout()

        # Creating Links
        link_label = QLabel()
        link_label.setText("Enter a link: ")
        self.link = QLineEdit()

        layout2.addWidget(link_label)
        layout2.addWidget(self.link)

        main_layout.addLayout(layout2)
        add = QPushButton('Add')
        main_layout.addWidget(add)
        add.clicked.connect(self.get_name_button)
        add.clicked.connect(self.close)


        self.setLayout(main_layout)


    def get_name_button(self):
        CreateBookspace.addLink(self.link.text())
        return self.link.text()



def run():
    app = QApplication(sys.argv)
    ex = AddLinks()
    ex.show()
    sys.exit(app.exec_())

#run()
