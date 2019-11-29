#!/usr/bin/python

from Tkinter import *
from ttk import *

class CustomBaseWidget:
    def __init__(self, widget, draggable, xPos, yPos):
        self.widget = widget
        self.draggable = draggable
        self.xPos = xPos
        self.yPos = yPos

    def makeDraggable(self):
        self.widget.bind("<Button-1>", self.onDragStart)
        self.widget.bind("<B1-Motion>", self.onDragMotion)

    def onDragStart(self, event):
        if(self.draggable):
            widget = event.widget
            widget._drag_start_x = event.x
            widget._drag_start_y = event.y

    def onDragMotion(self, event):
        if(self.draggable):
            widget = event.widget
            x = widget.winfo_x() - widget._drag_start_x + event.x
            y = widget.winfo_y() - widget._drag_start_y + event.y
            self.xPos = x
            self.yPos = y
            widget.place(x=x, y=y)

    def hide(self):
        self.widget.place_forget()

    def show(self):
        self.widget.grid()
        self.widget.place(x=self.xPos, y=self.yPos)