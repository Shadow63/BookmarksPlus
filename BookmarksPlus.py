from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys

def main():
    print('Starting up Bookmarks Plus Command-Line Interface...\n\n\n')

    print('Welcome to Bookmarks Plus!!! Here are your current active scripts:')
    # Gonna need to load up all existing scripts
    # Print out their names

    command = None
    while command.lower() != 'exit':
        command = input('Type \'run scriptname\' (where scriptname is your ACTUAL script name from the '
              'list above) to run a script!\n'
              'Type \'exit\' to quit.')



if __name__ == '__main__':
    main()