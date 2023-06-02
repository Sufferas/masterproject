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

    # Erstelle ein Text-Widget
    text_widget = tk.Text(root, wrap='word', font=('Arial', 12), bg=root.cget('bg'), relief='flat', state='disabled')
    text_widget.pack(fill='both', expand=True)

    # Text in das Text-Widget einfügen
    text_widget.configure(state='normal')
    text_widget.insert('1.0', text_to_display)
    text_widget.configure(state='disabled')

    # Funktion zum Kopieren des ausgewählten Textes
    def copy_text():
        try:
            # Kopiere den ausgewählten Text in die Zwischenablage
            root.clipboard_clear()
            root.clipboard_append(text_widget.selection_get())
        except tk.TclError:
            # Kein Text ausgewählt
            pass

    # Füge die Kopierfunktion zur rechten Maustaste hinzu
    text_widget.bind('<Button-3>', lambda e: copy_text())

    # Starte die Hauptloop
    root.mainloop()
