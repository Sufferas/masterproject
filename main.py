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


import time
import tkinter as tk
import threading
from pubsub import pub

lock = threading.Lock()


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.label = tk.Label(root, text="Temperature / Humidity")
        self.label.pack(side="top", fill="both", expand=True)

    def listener(self, plot_data):
        with lock:
            """do your plot drawing things here"""
            self.label.configure(text=plot_data)


class WorkerThread(threading.Thread):
    def __init__(self):
        super(WorkerThread, self).__init__()
        self.daemon = True  # do not keep thread after app exit
        self._stop = False

    def run(self):
        """calculate your plot data here"""
        for i in range(100):
            if self._stop:
                break
            time.sleep(1)
            pub.sendMessage('update', text=str(i))


if __name__ == '__main__':
    root = tk.Tk()
    root.wm_geometry("320x240+100+100")

    main = MainApplication(root)
    main.pack(side="top", fill="both", expand=True)

    pub.subscribe(main.listener, 'update')

    wt = WorkerThread()
    wt.start()

    root.mainloop()

    print("Welcome, you can now edit files or codes also via voice control.")
    from_microphone()

    # while True:
    #     start_point()


    # open_read_file('File2.py')
    # open_write_file('File2.py')