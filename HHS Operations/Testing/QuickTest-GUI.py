# !Python3                                              A3R0NA$
import os
from tkinter import *
from tkinter import messagebox

# Create main window
root = Tk()
root.title('Main Window')
root.geometry('200x200')


def PrintEntry():
    entry = entry_in.get()
    if len(entry) == 5:
        Label(root, text=entry).grid(row=3, column=0, columnspan=2)
    else:
        Label(root, text='Nope').grid(row=3, column=0, columnspan=2)


label = Label(root, text='Entry Box').grid(row=0, column=0)
entry_in = StringVar()
entry_box = Entry(root, width=20, textvariable=entry_in).grid(row=0, column=1)
button = Button(root, text='Print It', command=PrintEntry).grid(
    row=1, column=0, columnspan=2)
quit_button = Button(root, text='Exit').grid(row=7, column=0, columnspan=4)


# Run main logic (Open root window)
root.mainloop()
