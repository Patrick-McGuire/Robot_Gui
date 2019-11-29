#!/usr/bin/python

import RobotGUI

a = RobotGUI.RobotGUI("Nathan Is Pretty")

while (True):
    b = raw_input("Enter something: ")
    c = raw_input("Enter something else: ")

    a.data = {"heading": b, 'test4': c, 'tor': 0}
