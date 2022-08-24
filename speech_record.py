import speech_recognition as sr
import pyaudio

file_name = "audio/long.wav"
speech_engine = sr.Recognizer()


def from_file(file_name):
    with sr.AudioFile(file_name) as f:
        data = speech_engine.record(f)
        text = speech_engine.recognize_google(data, language="de-DE")
        return text


def from_microphone():
    with sr.Microphone() as micro:
        print("Recording...")
        audio = speech_engine.record(micro, duration=5)
        print("Recognition...")
        text = speech_engine.recognize_google(audio, language="de-DE")
        return text



def read_py_data():
    datei = open('main.py','r')
    print(datei.read(2))
# print(from_file(file_name))
#print(from_microphone())
read_py_data()
