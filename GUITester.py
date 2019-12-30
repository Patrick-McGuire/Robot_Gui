#!/usr/bin/python

import time
from GUIHandler import GUIHandler
import random
import cv2

a = GUIHandler("config/BasicConfig.xml")
dataPassDictionary = a.getDataPassDict()
# print (dataPassDictionary)
cap = cv2.VideoCapture(0)
lastSpinny = 0
spinnySign = 1
while a.handleQuit(False):
    keys = dataPassDictionary.keys()
    for key in keys:
        if key != "webcam" and key != "fullLoopTime" and key != "spinny" and key != "frameRate":
            dataPassDictionary[key] = random.randint(10, 19)

    if(random.randint(0,98) > 95):
        spinnySign = spinnySign * -1
    lastSpinny += (random.randint(0,100)) * spinnySign * .1 
    dataPassDictionary["spinny"] = lastSpinny

    # Get next image
    _, frame = cap.read()
    dataPassDictionary["webcam"] = frame

    a.updateInfo(dataPassDictionary)

    time.sleep(.025)
