from deepLearning.chat import get_trained_model
from speech_record import from_microphone
import time
from tkinter import ttk
import os


def path_file(path):
    cur_path = os.path.dirname(__file__)
    full_path = os.path.relpath(path, cur_path)
    return full_path


def voice_loop(dict_tk):
    print("Start voice function loop")

    while True:
        # print("What do you want to do")
        # voice_to_text = from_microphone()
        # text = get_trained_model(path_file("deepLearning\\TrainedModels\\file_command_task.pth"), path_file('deepLearning\\jsonFiles\\file_command_task.json'), voice_to_text)
        # text = get_trained_model("..\\deepLearning\\TrainedModels\\file_command_task.pth",
        #                          '..\\deepLearning\\jsonFiles\\file_command_task.json', voice_to_text)

        text = "add"
        time.sleep(2)

        dict_tk["system_help_text"].config(text=text)
        dict_tk["voice_recording_output_text"].config(text=text)

        if "cmd" == text:  # replace "edit new file" with a Command
            pass
        elif "edit" == text:
            pass
        elif "add" == text:
            create_file(dict_tk)
        else:
            print("Command not found")


def edit_file():
    pass



def character_input(dict_tk):

    print("Start Carakter")
    time.sleep(5)

    output_text = ""
    while True:
        voice_to_text = from_microphone()
        dict_tk["voice_recording_output_text"].config(text=voice_to_text)
        text = ""
        status, text = get_trained_model("..\\deepLearning\\TrainedModels\\ascii.pth",
                                         '..\\deepLearning\\jsonFiles\\ascii.json', voice_to_text)

        print(status, text)
        if status is False:
            continue
        if "stop " == text:
            print(output_text)
            time.sleep(10)
            return
        elif "delete" == text:
            if len(output_text) > 0:
                output_text = output_text.rstrip(output_text[-1])
            dict_tk["line_output_text"].config(text=output_text)
        else:
            output_text = output_text + text
            dict_tk["line_output_text"].config(text=output_text)






def get_file_name(dict_tk):
    print("Do you want to spell it out or say it word for word?")
    dict_tk["system_help_text"].config(text="Do you want to spell it out or say it word for word? Say exit to return")
    while True:
        voice_to_text = from_microphone()
        dict_tk["voice_recording_output_text"].config(text=voice_to_text)
        text = ""
        status, text = get_trained_model("..\\deepLearning\\TrainedModels\\word_or_letters.pth", '..\\deepLearning\\jsonFiles\\word_or_letters.json', voice_to_text)
        if status is False:
            continue

        if text == "exit":
            return
        if text == "word":
            pass
        elif text == "character":
            print("character option")
            character_input(dict_tk)

        else:
            print("statement could not be understood: \nHelp: say (word) or (character) or (exit)")
            dict_tk["user_help_text"].config(
                text="statement could not be understood: \nHelp: say (word) or (character) or (exit)")



def create_file(dict_tk):
    get_file_name(dict_tk)
    try:
        f = open("demofile3.txt", "r")
        f.close()
        print("File are existing: should the file be overwritten?")
    except:

        f = open("demofile3.txt", "w")
        print("file successfully created")
        f.close()

