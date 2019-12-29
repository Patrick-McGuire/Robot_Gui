#!/usr/bin/python

from Tkinter import *
import threading
from XmlParser import XmlParser
import time
from XMLOutput import XMLOutput
import Tkinter, Tkconstants, tkFileDialog

class RobotGUI(threading.Thread):
    filledDataPass = {}
    dataPassDictionary = {}
    filePath = ""
    enable = True
    count = 0

    def __init__(self, filePath):
        self.filePath = filePath
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        # Init the window
        self.window = Tk()

        self.parser = XmlParser(self.filePath, self.window)
        self.parser.guiGenerator.setParser(self.parser)
        self.allWidgetsList = self.parser.getAllWidgetsList()
        self.dataPassDictionary = self.parser.getDataPassDictionary()

        # scrollbar = Scrollbar(self.window)
        # scrollbar.pack(side=RIGHT, fill=Y)

        self.window.after(100, self.updateInfo)

        self.window.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.window.mainloop()

    def onClosing(self):
        self.enable = False

    def updateInfo(self):
        try:
            self.window.getint()
        except AttributeError:
            return

        # Update all widgets
        for widget in self.allWidgetsList:
            # Check to make sure there is actually data
            if self.filledDataPass == 0:
                pass
            elif len(self.filledDataPass) == 0:
                pass
            else:
                widget.updateInfo(self.filledDataPass)

            # Set this function to run again DON'T CHANGE TIME HERE
        self.window.after(10, self.updateInfo)

        # Check if the main thread has ended, and if it has, quit the window
        for i in threading.enumerate():
            if i.name == "MainThread":
                if not i.is_alive():
                    self.enable = False
                    self.window.destroy()

    def getDataPassDictionary(self):
        return self.dataPassDictionary

    def setDataPassDictionary(self, data):
        self.filledDataPass = data