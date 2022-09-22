import tkinter as tk
from tkinter import ttk
import time
import threading


def five_seconds():
    time.sleep(5)
    print("hallo")


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1400x1100")
        self.title('voice controlled editor')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)

        self.create_widgets()

    def create_widgets(self):
        dict_tk = {}
        rules = ttk.Label(self, text="Momentary task", style='Heading.TLabel')
        rules.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5, columnspan=2)

        edit_file_label = ttk.Label(self, text="File to edit: ")
        edit_file_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        edit_file_text = ttk.Label(self, text="no file selected: tell the file direktory, name and the format. ")
        edit_file_text.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        dict_tk["edit_file_text"] = edit_file_text

        line_being_edited_label = ttk.Label(self, text="line being edited: x")
        line_being_edited_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        dict_tk["line_being_edited_label"] = line_being_edited_label
        line_being_edited_text = ttk.Label(self, text="")
        line_being_edited_text.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
        dict_tk["line_being_edited_text"] = line_being_edited_text

        voice_recording_output_label = ttk.Label(self, text="voice recording output: ")
        voice_recording_output_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        voice_recording_output_text = ttk.Label(self, text="")
        voice_recording_output_text.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        dict_tk["voice_recording_output_text"] = voice_recording_output_text

        system_help_head = ttk.Label(self, text="The system requires special conmandos in some cases so that no information is lost and can be stored.", style='Heading.TLabel')
        system_help_head.grid(column=0, row=4, sticky=tk.N, padx=5, pady=5, columnspan=2)
        system_help_label = ttk.Label(self, text="System says: ", style='system_help.TLabel')
        system_help_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        system_help_text = ttk.Label(self, text="No file detect", style='system_help.TLabel')
        system_help_text.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
        dict_tk["system_help_text"] = system_help_text

        for i in range(40):

            add_rows_from_top = 6
            globals()[f"lines_{i}_label"] = ttk.Label(self, text=f"line:  {i} ")
            globals()[f"lines_{i}_label"].grid(column=0, row=add_rows_from_top+i, sticky=tk.W, padx=5, pady=1)
            dict_tk[f"lines_{i}_label"] = globals()[f"lines_{i}_label"]
            globals()[f"lines_{i}_text"] = ttk.Label(self, text="xxxxxxxxxxxxxx")
            globals()[f"lines_{i}_text"].grid(column=1, row=add_rows_from_top+i, sticky=tk.W, padx=5, pady=1)
            dict_tk[f"lines_{i}_text"] = globals()[f"lines_{i}_text"]

        self.style = ttk.Style(self)
        self.style.configure('Heading.TLabel', font=('Helvetica', 12))
        self.style.configure('system_help.TLabel', font=('Helvetica', 10))

        threading.Thread(target=five_seconds).start()


if __name__ == "__main__":
    app = App()
    app.mainloop()
