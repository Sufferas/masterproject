from deepLearning.chat import get_trained_model
from edit_file import open_read_file, open_write_file
from speech_record import from_microphone
from tkinter import *

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

    print("\\")
    print("Welcome, you can now edit files or codes also via voice control.")
    # from_microphone()
    while True:
        voice_to_text = from_microphone()
        print(voice_to_text)
        status, text = get_trained_model("deepLearning\\TrainedModels\\ascii.pth",
                                         'deepLearning\\jsonFiles\\ascii.json', voice_to_text)
        print(text)

    # while True:
    #     start_point()


    # open_read_file('File2.py')
    # open_write_file('File2.py')