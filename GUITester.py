#!/usr/bin/python
import time
from GUIHandler import GUIHandler
import random
import cv2

a = GUIHandler("config/BasicConfig.xml")
dataPassDictionary = a.getDataPassDict()
cap = cv2.VideoCapture(0)

while (a.handleQuit(False)):
    keys = dataPassDictionary.keys()
    for key in keys:
        if key != "webcam":
            dataPassDictionary[key] = random.randint(0, 9)

    _, frame = cap.read()
    dataPassDictionary["webcam"] = frame

    a.updateInfo(dataPassDictionary)

    time.sleep(.01)
