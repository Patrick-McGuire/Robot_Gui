#!/usr/bin/python

import time
from GUIHandler import GUIHandler
import random
import cv2

a = GUIHandler("config/BasicConfig.xml")
dataPassDictionary = a.getDataPassDict()
print (dataPassDictionary)
cap = cv2.VideoCapture(0)

while a.handleQuit(False):
    keys = dataPassDictionary.keys()
    for key in keys:
        if key != "webcam" or key != "fullLoopTime":
            dataPassDictionary[key] = random.randint(10, 19)

    # Get next image
    _, frame = cap.read()
    dataPassDictionary["webcam"] = frame

    a.updateInfo(dataPassDictionary)

    time.sleep(.025)
