#!/usr/bin/python

import ttk
from Tkinter import *
from ttk import *
import threading


class MyTkApp(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        a =Tk()
        lbl1 = Label(text="Test12", borderwidth=4, relief="raised", font=("Arial", 20))
        lbl1.grid(column=0, row=0)
        a.mainloop()


app = MyTkApp()
app.start()

print("Hi")


