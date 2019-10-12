class Bookspace:
    def __init__(self):
        pass

    names = ['hello', 'hi', 'hey']

    with open('bookspaces.txt', 'w') as file:
        for i in range(0, len(names)):
            file.write(names[i] + '\n')

    with open('bookspaces.txt') as file:
        bookspacesList = file.readlines()

    print(bookspacesList)
