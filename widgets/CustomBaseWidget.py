#!/usr/bin/python

from Tkinter import *
from ttk import *

class CustomBaseWidget:
    def __init__(self):
        pass

    def makeDraggable(self, widget):
        widget.bind("<Button-1>", self.onDragStart)
        widget.bind("<B1-Motion>", self.onDragMotion)

    def onDragStart(self, event):
        widget = event.widget
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y

    def onDragMotion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y() - widget._drag_start_y + event.y
        widget.place(x=x, y=y)
