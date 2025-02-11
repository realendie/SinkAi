import tkinter
from tkinter import *
import webbrowser
import subprocess

def callback(url):
    webbrowser.open_new(url)

root = Tk()
root.title("SinkAi")
root.geometry("800x800")

# Header // Author Link

heading = Label(root, text="SinkAi", font=("arial", 40, "bold"), fg="black").pack()

author = Label(root, text="By: @realendie", font=("arial", 10, "bold"), fg="black", cursor="hand2")
author.bind("<Button-1>", lambda e: callback("https://github.com/realendie"))
author.pack()

root.mainloop()