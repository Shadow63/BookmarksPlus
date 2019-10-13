from selenium import webdriver
import os


class BookspacesData:
    def __init__(self):
        pass

    bookspaces_data_file = 'bookspaces.txt'
    randomVar = 8

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
    def add_bookspace(bookspace_name, urls, usernames, passwords, is_focused, has_next):
        bookspaces_list = BookspacesData.get_bookspaces()

        # Checks if name is a duplicate
        if bookspace_name not in bookspaces_list:
            with open(BookspacesData.bookspaces_data_file, 'a') as f:
                f.write(bookspace_name + '\n')
            file_ptr = open('scripts/' + bookspace_name + '.py', 'a')

            # Creating script file, only if there are links
            if len(urls) > 0:
                init_sleep_time = 5
                after_username_sleep_time = 1
                enter_sleep_time = 3

                file_ptr.write(
"""from selenium import webdriver
import pyautogui
import time

browser = webdriver.Firefox()
browser.get('""" + urls[0] + "')\n")

                # Handling logins, only if there are more than 1 login credentials
                if len(usernames[0]) > 0 and not is_focused[0] and not has_next[0]:
                    file_ptr.write(
"""time.sleep(""" + str(init_sleep_time) + ")\n" + """
pyautogui.press('tab')
time.sleep(1)
pyautogui.typewrite('""" + usernames[0] +
"')\n" + """time.sleep(1)\npyautogui.press('tab')\npyautogui.typewrite('""" + passwords[0] + "')\n" +
"pyautogui.press('enter')\n\n")
                if len(usernames[0]) > 0 and is_focused[0] and not has_next[0]:
                    file_ptr.write(
"""time.sleep(""" + str(init_sleep_time) + ")\n" + """
pyautogui.typewrite('""" + usernames[0] +
"')\n" + """time.sleep(1)\npyautogui.press('tab')\npyautogui.typewrite('""" + passwords[0] + "')\n" +
"pyautogui.press('enter')\n\n")
                if len(usernames[0]) > 0 and not is_focused[0] and has_next[0]:
                    file_ptr.write(
"""time.sleep(""" + str(init_sleep_time) + ")\n" + """
pyautogui.press('tab')
time.sleep(1)
pyautogui.typewrite('""" + usernames[0] +
"')\npyautogui.press('enter')\ntime.sleep(" + str(enter_sleep_time) + ")\npyautogui.typewrite('" + passwords[0] + "')\n" +
"pyautogui.press('enter')\n\n")
                if len(usernames[0]) > 0 and is_focused[0] and has_next[0]:
                    file_ptr.write(
"""time.sleep(""" + str(init_sleep_time) + ")\n" + """
pyautogui.typewrite('""" + usernames[0] +
"')\npyautogui.press('enter')\n" + """time.sleep(""" + str(enter_sleep_time) + ")\npyautogui.typewrite('""" + passwords[
    0] + "')\n" +
"pyautogui.press('enter')\n\n")

                for i in range(1, len(urls)):
                    open_url_script = 'window.open("' + urls[i] + '", "_blank")'

                    # Write to script file
                    file_ptr.write("browser.execute_script('" + open_url_script + "')\n")

                    if len(usernames[i]) > 0 and not is_focused[i] and not has_next[i]:
                        file_ptr.write(
"""time.sleep(""" + str(init_sleep_time) + ")\n" + """
pyautogui.press('tab')
time.sleep(1)
pyautogui.typewrite(""" + usernames[i] +
")\n" + """time.sleep(1)\npyautogui.press('tab')\npyautogui.typewrite(""" + passwords[i] + ")\n" +
"pyautogui.press('enter')\n\n")
                    if len(usernames[i]) > 0 and is_focused[i] and not has_next[i]:
                        file_ptr.write(
"""time.sleep(""" + str(init_sleep_time) + ")\n" + """
pyautogui.typewrite('""" + usernames[i] +
"')\n" + """time.sleep(1)\npyautogui.press('tab')\npyautogui.typewrite('""" + passwords[i] + "')\n" +
"pyautogui.press('enter')\n\n")
                    if len(usernames[i]) > 0 and not is_focused[i] and has_next[i]:
                        file_ptr.write(
"""time.sleep(""" + str(init_sleep_time) + ")\n" + """
pyautogui.press('tab')
time.sleep(1)
pyautogui.typewrite('""" + usernames[i] +
"')\npyautogui.press('enter')\ntime.sleep(" + str(enter_sleep_time) + ")\npyautogui.typewrite('" + passwords[i] + "')\n" +
"pyautogui.press('enter')\n\n")
                    if len(usernames[i]) > 0 and is_focused[i] and has_next[i]:
                        file_ptr.write(
"""time.sleep(""" + str(init_sleep_time) + ")\n" + """
pyautogui.typewrite('""" + usernames[i] +
"')\npyautogui.press('enter')\n" + """time.sleep(""" + str(enter_sleep_time) + ")\npyautogui.typewrite('""" +
passwords[i] + "')\n" +
"pyautogui.press('enter')\n\n")
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
