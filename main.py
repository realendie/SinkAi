import tkinter
from tkinter import *
from tkinter.font import Font
import webbrowser
import subprocess
import sv_ttk
import darkdetect


def callback(url):
    webbrowser.open_new(url)


font = Font(file="Geologica-VariableFont_CRSV,SHRP,slnt,wght.ttf", family=font)


root = tkinter.Tk()
root.title("SinkAi")
root.geometry("800x600")

# Header // Author Link

heading = tkinter.Label(root, text="SinkAi", font=(font, 10, "bold"), fg="black").pack()

author = tkinter.Label(
    root,
    text="By: @realendie",
    font=(font, 10, "bold"),
    fg="black",
    cursor="hand10",
)
author.bind("<Button-1>", lambda e: callback("https://github.com/realendie"))
author.pack()

# Input Box

response_box = tkinter.Text(
    root, width=100, font=(font, 10), fg="black", state=DISABLED
)
response_box.pack()

input_label = tkinter.Label(root, text="Input:", font=(font, 10), fg="black").pack()

input_box = tkinter.Text(root, font=(font, 10), fg="black").pack()

sv_ttk.set_theme(darkdetect.theme())

root.mainloop()
