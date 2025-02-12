import tkinter
from tkinter import *
from tkinter.font import Font
import webbrowser
import subprocess
import sv_ttk
import darkdetect


def callback(url):
    webbrowser.open_new(url)
def set_text():
    response = "Hello this is sample text!"
    response_box.config(state=NORMAL)
    response_box.insert(END, response)
    response_box.config(state=DISABLED)


TESsT = "Test"

root = tkinter.Tk()
root.title("SinkAi")
root.geometry("800x700")

# Header // Author Link

heading = tkinter.Label(root, text="SinkAi", font=('Segoe UI', 20, "bold"), fg="black").pack()

author = tkinter.Label(
    root,
    text="By: @realendie",
    font=('Segoe UI', 10, "bold"),
    fg="black",
    cursor='hand2',
)
author.bind("<Button-1>", lambda e: callback("https://github.com/realendie"))
author.pack()

# Input Box

response_box = tkinter.Text(
    root, width=100, font=('Segoe UI', 10), fg="black", state=DISABLED,
)
response_box.pack()

input_label = tkinter.Label(root, text="Input:", font=('Segoe UI', 10, "bold"), fg="black").pack()

input_box = tkinter.Entry(root, font=('Segoe UI', 10), fg="black", width='100').pack()

submit_button = tkinter.Button(root, text="Submit", font=('Segoe UI Semibold', 10), fg="black", command=set_text)
submit_button.pack()

sv_ttk.set_theme(darkdetect.theme())

root.mainloop()
