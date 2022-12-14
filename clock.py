import tkinter as Tkinter
from datetime import datetime

counter = 66600
running = False


def counter_label(label):
    def count():
        if running:
            global counter

            if counter == 66600:
                display = "starting"
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string

            label['text'] = display
