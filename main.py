import tkinter
from tkinter import *
from tkinter import ttk
import webbrowser
import subprocess
import sv_ttk


def callback(url):
    webbrowser.open_new(url)


sv_ttk.set_theme("dark")

root = tkinter.Tk()
root.title("SinkAi")
root.geometry("800x600")

# Header // Author Link

heading = ttk.Label(root, text="SinkAi", font=("arial", 40, "bold"), fg="black").pack()

author = ttk.Label(
    root, text="By: @realendie", font=("arial", 10, "bold"), fg="black", cursor="hand2"
)
author.bind("<Button-1>", lambda e: callback("https://github.com/realendie"))
author.pack()

# Input Box

response_box = ttk.Text(
    root, width=100, font=("Monoscape", 10), fg="black", state=DISABLED
)
response_box.pack()

serperator = ttk.Label(
    root, text="==============================", font=("Monoscape", 10), fg="black"
).pack()

input_box = ttk.Text(root, font=("Monoscape", 10), fg="black").pack()

root.mainloop()
