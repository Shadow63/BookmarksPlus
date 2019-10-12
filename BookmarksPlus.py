from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 300, 300)
    win.setWindowTitle('Bookmarks Plus!')

    label = QtWidgets.QLabel(win)
    label.setText("Test")
    label.move(50, 50)

    win.show()
    sys.exit(app.exec_())


def main():
    print('Starting up Bookmarks Plus Command-Line Interface...\n\n\n')

    print('Welcome to Bookmarks Plus!!! Here are your current active scripts:')
    # Gonna need to load up all existing scripts
    # Print out their names

    command = 'none'
    while command.lower() != 'exit':
        command = input('Type \'run scriptname\' (where scriptname is your ACTUAL script name from the '
              'list above) to run a script!\n'
              'Type \'qt\' to run the GUI interface.\n'
              'Type \'exit\' to quit.\n>>>')
        if command == 'exit':
            break
        elif command == 'qt':
            window()


if __name__ == '__main__':
    main()