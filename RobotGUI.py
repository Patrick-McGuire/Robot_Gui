#!/usr/bin/python

import ttk
from Tkinter import *
from ttk import *
import random
import threading
from widgets import ConfigurableTextBoxWidget


class RobotGUI(threading.Thread):
    box1 = ""
    data = {"heading": 0, 'test4': 0, 'tor': 0}

    def __init__(self, guiName):
        self.guiName = guiName

        threading.Thread.__init__(self)
        self.start()

    def run(self):
        # Init the window
        self.window = Tk()
        self.window.title(self.guiName)
        self.window.geometry('1920x1080')

        # Create tabs
        tab_control = ttk.Notebook(self.window)
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Dashboard')
        tab_control.add(tab2, text='Settings')

        configInfo = [['Heading', 'heading'], ['Battery', 'test4'], ['aslkd', 'tor'], ['eee', 'test4']]
        a = {"title": "Robot Information", "tab": tab1, "font": "Arial", "xPos": 5, "yPos": 5, "config": configInfo}

        self.Box1 = ConfigurableTextBoxWidget.ConfigurableTextBoxWidget(a)

        tab_control.pack(expand=1, fill='both')
        self.window.after(100, self.updateInfo)
        self.window.mainloop()

    def updateInfo(self):
        self.Box1.updateInfo(self.data)

        self.window.after(100, self.updateInfo)
