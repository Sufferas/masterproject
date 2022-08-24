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
    print("Enter path + file name")
    print("say back or zurueck to jump back one character")
    print("For memory they say save or apply")

    # TODO Record
    save_path = False
    save_path_name = ""
    #while save_path is False:
