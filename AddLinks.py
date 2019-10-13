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
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()

        # Creating Links
        link_label = QLabel()
        link_label.setText("Enter a link: ")
        self.link = QLineEdit()

        layout2.addWidget(link_label)
        layout2.addWidget(self.link)

        # Creating Usernames
        username_label = QLabel()
        username_label.setText("Enter the Username: ")
        self.username = QLineEdit()

        layout3.addWidget(username_label)
        layout3.addWidget(self.username)

        # Creating Passwords
        password_label = QLabel()
        password_label.setText('Enter the Password: ')
        self.password = QLineEdit()

        layout4.addWidget(password_label)
        layout4.addWidget(self.password)


        main_layout.addLayout(layout2)
        main_layout.addLayout(layout3)
        main_layout.addLayout(layout4)
        add = QPushButton('Add')
        main_layout.addWidget(add)

        add.clicked.connect(self.get_link_button)
        add.clicked.connect(self.get_username_button)
        add.clicked.connect(self.get_password_button)
        add.clicked.connect(self.close)

        self.setLayout(main_layout)


    def get_link_button(self):
        CreateBookspace.addLink(self.link.text())
        return self.link.text()

    def get_username_button(self):
        CreateBookspace.addUsername(self.username.text())
        return self.username.text()

    def get_password_button(self):
        CreateBookspace.addPassword(self.password.text())
        return self.password.text()



def run():
    app = QApplication(sys.argv)
    ex = AddLinks()
    ex.show()
    sys.exit(app.exec_())

#run()
