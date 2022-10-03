from deepLearning.chat import get_trained_model
from speech_record import from_microphone


def voice_loop(dict_tk):
    print("Start voice function loop")
    while True:
        print("What do you want to do")
        from_microphone()
        get_trained_model("trained_model", "json_file", "input_string")
        if "edit new file" == "edit new file":  # replace "edit new file" with a Command
            return
