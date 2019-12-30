#!/usr/bin/python
from Tkinter import *


def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)

master = Tk()

w = Canvas(master, width=400, height=400)
w.grid(column=0, row=0)

make_draggable(w)

w.create_text(10,10,text="fds")

mainloop()