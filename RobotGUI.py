#!/usr/bin/python

from Tkinter import *
import threading
from XmlParser import XmlParser
from Constants import *


class RobotGUI(threading.Thread):
    filledDataPass = {}
    dataPassDictionary = {}
    filePath = ""

    def __init__(self, filePath):
        self.filePath = filePath
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        # Init the window
        self.window = Tk()
        self.window.geometry('1920x1080')

        self.parser = XmlParser(self.filePath, self.window)
        self.allWidgetsList = self.parser.getAllWidgetsList()
        self.dataPassDictionary = self.parser.getDataPassDictionary()

        self.window.after(100, self.updateInfo)
        self.window.mainloop()

    def updateInfo(self):
        #print(self.allWidgetsList)
        for widget in self.allWidgetsList:
            widget.updateInfo(self.filledDataPass)
        self.window.after(50, self.updateInfo)

    def getDataPassDictionary(self):
        return self.dataPassDictionary

    def setDataPassDictionary(self, data):
        self.filledDataPass = data


