#!/usr/bin/python
import time
from GUIHandler import GUIHandler

a = GUIHandler("config/BasicConfig.xml")
while(a.handleQuit(False)):
    a.simUpdateInfo()
    time.sleep(.01)
