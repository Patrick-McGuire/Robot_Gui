#!/usr/bin/python

import Tkinter
import threading
import time
from Tkinter import TclError

from XmlParser import XmlParser


class RobotGUI(threading.Thread):
    def __init__(self, filePath):
        self.filledDataPass = {}
        self.dataPassDictionary = {}
        self.filePath = ""
        self.enable = True
        self.count = 0
        self.lastTime = 0

        self.filePath = filePath
        self.frameRate = float(30)
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        # Init the window
        self.window = Tkinter.Tk()
        self.window.minsize(100, 100)

        self.parser = XmlParser(self.filePath, self.window)
        self.parser.guiGenerator.setParser(self.parser)
        self.allWidgetsList = self.parser.getAllWidgetsList()
        self.dataPassDictionary = self.parser.getDataPassDictionary()

        self.window.after(100, self.updateInfo)

        self.window.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.window.mainloop()

    def onClosing(self):
        self.enable = False

    def updateInfo(self):
        # Frame rate measurer
        startTime = time.time()
        fullLoopTime = startTime - self.lastTime
        self.lastTime = startTime

        self.filledDataPass["fullLoopTime"] = int(fullLoopTime * 1000)
        self.filledDataPass["frameRate"] = int(1 / fullLoopTime)

        # Update info
        try:
            self.window.getint()
        except (AttributeError, TclError) as e:
            print(e)

        # Update all widgets
        for widget in self.allWidgetsList:
            # Check to make sure there is actually data
            if self.filledDataPass == 0 or len(self.filledDataPass) == 0:
                pass
            elif widget.isHidden:
                pass
            else:
                widget.updateInfo(self.filledDataPass)

        # Check if the main thread has ended, and if it has, quit the window
        for i in threading.enumerate():
            if i.name == "MainThread":
                if not i.is_alive():
                    self.enable = False
                    self.window.destroy()

        # Frame rate controller
        desiredLoopTime = 1 / self.frameRate
        currentTime = time.time()
        loopTime = currentTime - startTime
        timeDelta = (desiredLoopTime - loopTime) * 1000
        if timeDelta < 1:
            timeDelta = 1

        # Set this function to run again
        self.window.after(int(timeDelta), self.updateInfo)

    def getDataPassDictionary(self):
        return self.dataPassDictionary

    def setDataPassDictionary(self, data):
        self.filledDataPass = data
