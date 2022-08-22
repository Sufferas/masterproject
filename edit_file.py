def open_read_file(name):
    try:
        file = open(name, 'r+')
        print("File could be opened successfully  ")
        return file
    except:
        print("File could not be opened or was not found.")


def open_write_file(name):
    try:
        file = open(name, 'w+')
        print("File could be opened successfully  ")
        return file
    except:
        print("File could not be created.")


def get_file_name():
    print()