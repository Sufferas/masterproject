from GUI.testsub import create_and_show_gui
from deepLearning.chat import get_trained_model
from edit_file import open_read_file, open_write_file
from speech_record import from_microphone
from tkinter import *
import trained_funktions_list


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


def search_function():
    voice_to_text = from_microphone()

    status, text = get_trained_model("deepLearning\\TrainedModels\\train_call_function.pth",
                                      'deepLearning\\jsonFiles\\train_call_function.json', voice_to_text)

    print(text)

    try:
        # Überprüfe, ob das Attribut im Modul existiert
        if hasattr(trained_funktions_list, text):
            # Wenn ja, rufe die Funktion auf
            function_call = getattr(trained_funktions_list, text)
            function_call(voice_to_text)
        else:
            print(f'Die Funktion {text} existiert nicht im Modul trained_funktions_list.')
    except AttributeError as e:
        print(f'Es gab einen Fehler: {e}')







if __name__ == '__main__':

    create_and_show_gui('Welcome, you can now edit files or codes also via voice control.', 3000)

    activation_text = "HELLO ALICE, HEY ALICE, HALLO ALICE, HELLO ELLIS, HEY ELLIS, HALLO ELLIS, HEY DU, HALLO DU"
    while True:
        voice_to_text = from_microphone()
        print(voice_to_text)
        upper_voice_to_text = voice_to_text.upper()
        # upper_voice_to_text = "HALLO ALICE"


        if activation_text.find(upper_voice_to_text) != -1:
            create_and_show_gui('How can I help you?', 2000)
            print(f"Das Wort '{upper_voice_to_text }' wurde gefunden.")
            search_function()

        else:
            print(f"Das Wort '{upper_voice_to_text}' wurde nicht gefunden.")


