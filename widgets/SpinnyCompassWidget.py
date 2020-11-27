#!/usr/bin/python

import os
import xml.etree.ElementTree as ET
from PIL import Image as PILImage
from PIL import ImageTk

from Constants import *
from CustomBaseWidget import *


class SpinnyCompassWidget(CustomBaseWidget):
    def __init__(self, configDict, window):
        self.configInfo = []
        self.type = Constants.COMPASS_TYPE
        self.lastAngle = 0

        self.window = window
        self.title = configDict[Constants.TITTLE_ATTRIBUTE]
        self.tab = configDict[Constants.TAB_ATTRIBUTE]
        self.xPos = configDict[Constants.X_POS_ATTRIBUTE]
        self.yPos = configDict[Constants.Y_POS_ATTRIBUTE]
        self.hidden = configDict[Constants.HIDDEN_ATTRIBUTE]
        self.draggable = configDict[Constants.DRAGGABLE_ATTRIBUTE]
        self.size = int(configDict[Constants.SIZE_ATTRIBUTE])
        self.source = configDict[Constants.SOURCE_ATTRIBUTE]

        self.filePath = os.path.dirname(os.path.realpath(__file__))

        shortFilePath = list(self.filePath)
        for i in range(len(shortFilePath) - 1, 0, -1):
            if shortFilePath.pop(i) == "/":
                break
        self.filePath = "".join(shortFilePath)

        # self.updateInfo(0)
        self.widget = Canvas(self.tab, width=self.size, height=self.size, bg="Black")
        self.createBaseImages()

        self.widget.grid(column=0, row=0)
        self.widget.place(x=self.xPos, y=self.yPos)

        CustomBaseWidget.__init__(self, self.widget, self.draggable, self.xPos, self.yPos, window, configDict[Constants.TITTLE_ATTRIBUTE], self.hidden)

    def createBaseImages(self):
        self.compassImage = PILImage.open(self.filePath + '/Assets/compass.png').resize((self.size, self.size), PILImage.ANTIALIAS)
        self.compassTkimage = ImageTk.PhotoImage(self.compassImage)
        self.compassCanvas_obj1 = self.widget.create_image(int(self.size / 2), int(self.size / 2), image=self.compassTkimage)

        self.arrowImage = PILImage.open(self.filePath + '/Assets/arrow.png')
        self.arrowImage = self.arrowImage.resize((int(self.size * 2.5), int(self.size * 1.25)), PILImage.ANTIALIAS)
        self.arrowTkimage = ImageTk.PhotoImage(self.arrowImage.rotate(0))
        self.canvas_obj = self.widget.create_image(int(self.size / 2), int(self.size / 2), image=self.arrowTkimage)

    def geterateAngledImage(self, angle):
        self.arrowTkimage = ImageTk.PhotoImage(self.arrowImage.rotate(angle))
        self.canvas_obj = self.widget.create_image(int(self.size / 2), int(self.size / 2), image=self.arrowTkimage)

    def updateInfo(self, data):
        try:
            angle = -(90 + float(data[self.source]))
            if (angle != self.lastAngle):
                self.geterateAngledImage(self.lastAngle)
                self.lastAngle = angle
        except KeyError:
            pass

    def getXMLStuff(self, item):
        tag = ET.SubElement(item, Constants.WIDGET_NAME)
        tag.set(Constants.TITTLE_ATTRIBUTE, str(self.title))
        tag.set(Constants.X_POS_ATTRIBUTE, str(self.xPos))
        tag.set(Constants.Y_POS_ATTRIBUTE, str(self.yPos))
        tag.set(Constants.HIDDEN_ATTRIBUTE, str(self.isHidden))
        tag.set(Constants.DRAGGABLE_ATTRIBUTE, str(self.draggable))
        tag.set(Constants.TYPE_ATTRIBUTE, str(self.type))
        tag.set(Constants.SIZE_ATTRIBUTE, str(self.size))
        tag.set(Constants.SOURCE_ATTRIBUTE, str(self.source))
