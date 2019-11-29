#!/usr/bin/python

import RobotGUI
from Constants import *
import random
import time

a = RobotGUI.RobotGUI("config/BasicConfig.xml")
time.sleep(1)
c = a.getDataPassDictionary()

print(c)

while (True):
    c[Constants.BATTERY_VOLTAGE_VALUE] = random.randint(0,9)
    c[Constants.V5_VOLTAGE_VALUE] = random.randint(0,9)
    c[Constants.V33_VOLTAGE_VALUE] = random.randint(0,9)
    c[Constants.CURRENT_VALUE] = random.randint(0,9)

    a.setDataPassDictionary(c)
    time.sleep(.05)