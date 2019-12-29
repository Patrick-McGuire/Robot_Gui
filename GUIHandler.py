#!/usr/bin/python

import RobotGUI
import random
import time
import warnings


class GUIHandler:
    def __init__(self, filePath):
        self.guiInstance = RobotGUI.RobotGUI(filePath)
        time.sleep(1)  # Allow for the other thread to complete initialization
        self.dataPassDictionary = self.guiInstance.getDataPassDictionary()
        warnings.filterwarnings("ignore")

    def updateInfo(self, passDict):
        self.guiInstance.setDataPassDictionary(passDict)

    def simUpdateInfo(self):
        keys = self.dataPassDictionary.keys()
        for key in keys:
            self.dataPassDictionary[key] = random.randint(0, 9)
        self.updateInfo(self.dataPassDictionary)

    def handleQuit(self, manualQuit):
        if not self.guiInstance.is_alive() or not self.guiInstance.enable or manualQuit:
            self.guiInstance.window.quit()
            return False
        return True

    def getDataPassDict(self):
        return self.dataPassDictionary
