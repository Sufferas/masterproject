from edit_file import open_read_file, open_write_file
from speech_record import from_microphone


def start_point():
    """
    Commands
    1. edit new file

    """

    file_name = ''
    file_is_not_set = True

    print("Which file should be edited")

    while file_is_not_set:
        # TODO add sprachenerkenung
        # file_name, file_is_not_set  = get_file_name()
        file_name = 'example.py'
        file_is_not_set = False

    while True:
        # TODO: Spracherkennung  command = get_command()
        # TODO: Commands

        if "edit new file" == "edit new file": # replace "edit new file" with a Command
            return






if __name__ == '__main__':

    print("Welcome, you can now edit files or codes also via voice control.")
    from_microphone()

    while True:
        start_point()


    # open_read_file('File2.py')
    # open_write_file('File2.py')