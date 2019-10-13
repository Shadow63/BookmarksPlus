from selenium import webdriver
import os


class BookspacesData:
    def __init__(self):
        pass

    bookspaces_data_file = 'bookspaces.txt'

    # Retrieves the list of bookspaces the user has created
    @staticmethod
    def get_bookspaces():
        file_length = len(open(BookspacesData.bookspaces_data_file, 'r').readlines())
        bookspaces_list = []

        with open(BookspacesData.bookspaces_data_file) as f:
            for i in range(0, file_length):
                bookspaces_list.append(f.readline()[:-1])

        return bookspaces_list

    # Adds a bookspace to the database
    @staticmethod
    def add_bookspace(bookspace_name, urls):
        bookspaces_list = BookspacesData.get_bookspaces()

        # Checks if name is a duplicate
        if bookspace_name not in bookspaces_list:
            with open(BookspacesData.bookspaces_data_file, 'a') as f:
                f.write(bookspace_name + '\n')

            file_ptr = open('scripts/' + bookspace_name + '.py', 'a')
            file_ptr.write(
"""from selenium import webdriver

browser = webdriver.Firefox()
browser.get('""" + urls[0] + "')\n\n")

            for i in range(1, len(urls)):
                open_url_script = 'window.open("' + urls[i] + '", "_blank")'

                # Write to script file
                file_ptr.write("browser.execute_script('" + open_url_script + "')\n")
        else:
            print('error: bookspace name already exists')

    # Deletes a bookspace from the database
    @staticmethod
    def delete_bookspace(bookspace_name):
        bookspaces_list = BookspacesData.get_bookspaces()

        # Checks if name exists, if it does then delete it, if not throw an error message
        if bookspace_name in bookspaces_list:
            bookspaces_list.remove(bookspace_name)
            os.remove('scripts/' + bookspace_name + '.py')
            with open(BookspacesData.bookspaces_data_file, 'w') as f:
                for i in range(0, len(bookspaces_list)):
                    f.write(bookspaces_list[i] + '\n')
        else:
            print('error: bookspace name does not exists')
