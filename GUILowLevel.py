#!/usr/bin/python

import Tkinter
import threading
import time
from Tkinter import TclError


class GUILowLevel(threading.Thread):
    def __init__(self, filePath, frameRate):
        self.dataPassDict = {}
        self.enable = True
        self.lastTime = 0

        self.filePath = filePath
        self.frameRate = float(frameRate)
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        # Create the window
        self.window = Tkinter.Tk()         # Create a Tkinter object
        self.window.minsize(100, 100)      # Set the minimum size the window can be

        # Create all the widgets
        self.parser = XmlParser(self.filePath, self.window)
        self.parser.guiGenerator.setParser(self.parser)
        self.allWidgetsList = self.parser.getAllWidgetsList()
        self.dataPassDictionary = self.parser.getDataPassDictionary()

        # Window flow control
        self.window.after(100, self.updateInfo)                       # Give it a function to run to update the window
        self.window.protocol("WM_DELETE_WINDOW", self.onClosing)      # Tell it what to do when you close the window
        self.window.mainloop()                                        # Create the window

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
        return self.dataPassDict

    def setDataPassDictionary(self, data):
        self.dataPassDict = data

