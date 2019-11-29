#!/usr/bin/python

import threading
import RobotGUI
from DataPass import DataPass


dataPass = DataPass()

def threadFunction():
    print("Hi")
    while(True):
        b = raw_input("Enter something: ")
        dataPass.set(b)


x = threading.Thread(target = threadFunction, name='t1')
x.start()

a = RobotGUI.RobotGUI("Nathan Sucks", dataPass)