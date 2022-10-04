from deepLearning.chat import get_trained_model
from speech_record import from_microphone
import time
from tkinter import ttk


def voice_loop(dict_tk):
    print("Start voice function loop")

    while True:
        # print("What do you want to do")
        # voice_to_text = from_microphone()
        # text = get_trained_model("TrainedModels/file_command_task.pth", 'jsonFiles/file_command_task.json', voice_to_text)

        text = "add"

        dict_tk["system_help_text"].config(text="5 Seconds is Up")

        if "cmd" == text:  # replace "edit new file" with a Command
            pass
        elif "edit" == text:
            pass
        elif "add" == text:
            create_file()
            pass
        else:
            print("Command not found")


def edit_file():
    pass


def get_file_name():
    pass


def create_file():
    get_file_name()
    try:
        f = open("demofile3.txt", "r")
        f.close()
        print("File are existing: should the file be overwritten?")
    except:

        f = open("demofile3.txt", "w")
        print("file successfully created")
        f.close()

