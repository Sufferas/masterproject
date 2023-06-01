from tkinter import *
import time
from random import randint
import threading

import tkinter as tk
import time

# root = Tk()
# root.title("See you file")
# root.geometry("500x400")
#
# def five_seconds():
#     time.sleep(5)
#     my_label.config(text="5 Seconds is Up")
#
# def rando():
#     random_label.config(text=f'Random Number: {randint(1,100)}')
#
#
# my_label = Label(root, text="Hello There")
# my_label.pack(pady=50)
# my_button1 = Button(root, text="5 Seconds", command=threading.Thread(target=five_seconds).start())
# my_button1.pack(pady=20)
#
# my_button2 = Button(root, text="pick random Number", command=rando)
# my_button2.pack(pady=20)
# random_label = Label(root, text="")
# random_label.pack(pady=20)
#
# root.mainloop()


def create_and_show_gui(text_to_display, time_to_close):
    # Erstelle ein neues Tkinter Fenster
    root = tk.Tk()
    root.title('Fenster')

    # Erstelle ein Label und zeige den Text an
    label = tk.Label(root, text=text_to_display, font=('Arial', 12), pady=10)
    label.pack()

    # Funktion zum Schließen des Fensters nach 5 Sekunden
    def close_window():
        root.destroy()

    # Setze einen Timer für die close_window-Funktion
    root.after(time_to_close, close_window)

    # Starte die Hauptloop
    root.mainloop()


def create_gui(text_to_display):
    # Erstelle ein neues Tkinter Fenster
    root = tk.Tk()
    root.title('Fenster')

    # Erstelle ein Label und zeige den Text an, setze die Schriftgröße auf 24
    label = tk.Label(root, text=text_to_display, font=('Arial', 12), pady=10)
    label.pack()

    # Starte die Hauptloop
    root.mainloop()
