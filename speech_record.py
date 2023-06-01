import speech_recognition as sr

speech_engine = sr.Recognizer()


def from_file(file_name):
    with sr.AudioFile(file_name) as f:
        data = speech_engine.record(f)
        text = speech_engine.recognize_google(data, language="de-DE")
        return text


def from_microphone():
    with sr.Microphone() as micro:
        try:
            print("Recording...")
            audio = speech_engine.record(micro, duration=5)
            print("Recognition...")
            #text = speech_engine.recognize_google(audio, language="en-EN")
            text = speech_engine.recognize_google(audio, language="de-DE")
            print("You said " + text)
            # text = speech_engine.recognize_google(audio, language="en-EN")
            return text
        except:
            return "no voice input detected"

