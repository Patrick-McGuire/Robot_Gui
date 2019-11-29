#!/usr/bin/python

import ttk
from Tkinter import *
from ttk import *
import random
import threading

class RobotGUI(threading.Thread):

    def __init__(self, guiName):
        self.dataPass = ""
        self.guiName = guiName

        threading.Thread.__init__(self)
        self.start()


    def run(self):
        # Init the window
        self.window = Tk()
        self.window.title(self.guiName)
        self.window.geometry('1920x1080')

        self.allWidgetInfo = []
        self.allWidgets = []

        # Create tabs
        tab_control = ttk.Notebook(self.window)
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Dashboard')
        tab_control.add(tab2, text='Settings')

        self.allWidgetInfo = [["Power Stats", StringVar(), 50, 50], ["Positional Stats", StringVar(), 100, 100], ["Bruh Momment", StringVar(), 150, 150]]
        self.allWidgets = []
        for i in range(0, len(self.allWidgetInfo)):
            self.allWidgetInfo[i][1].set("INIT")
            self.allWidgets.append(Label(tab1, textvariable = self.allWidgetInfo[i][1], borderwidth=4, relief="raised", font=("Arial", 20)))
            self.allWidgets[i].grid(column=0, row=0)
            self.allWidgets[i].place(x = self.allWidgetInfo[i][2], y = self.allWidgetInfo[i][3])
            self.makeDraggable(self.allWidgets[i])

        tab_control.pack(expand=1, fill='both')
        self.window.after(100, self.updateInfo)
        self.window.mainloop()

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
        widget.place(x = x, y = y)

    def updateInfo(self):
        data = self.dataPass
        for x in range(0, len(self.allWidgetInfo)):
            self.allWidgetInfo[x][1].set("{0}{1}".format(data, str(random.randint(0, 10))))
        self.window.after(100, self.updateInfo)

