#!/usr/bin/python

from CustomBaseWidget import *
from Constants import *
import xml.etree.ElementTree as ET
from PIL import ImageTk
from PIL import Image as PILImage


class SpinnyCompassWidget(CustomBaseWidget):
    configInfo = []
    type = Constants.COMPASS_TYPE
    heading = 0
    a = 0
    def __init__(self, configDict, window):
        self.window = window
        self.title = configDict[Constants.TITTLE_ATTRIBUTE]
        self.tab = configDict[Constants.TAB_ATTRIBUTE]
        self.xpos = configDict[Constants.X_POS_ATTRIBUTE]
        self.ypos = configDict[Constants.Y_POS_ATTRIBUTE]
        self.hidden = configDict[Constants.HIDDEN_ATTRIBUTE]
        self.draggabe = configDict[Constants.DRAGGABLE_ATTRIBUTE]
        self.size = int(configDict[Constants.SIZE_ATTRIBUTE])

        # self.updateInfo(0)
        self.widget = Canvas(self.tab, width=self.size, height=self.size, bg="Black")
        self.createBaseImages()

        self.widget.grid(column=0, row=0)
        self.widget.place(x=self.xpos, y=self.ypos)

        CustomBaseWidget.__init__(self, self.widget, self.draggabe, self.xpos, self.ypos, window, configDict[Constants.TITTLE_ATTRIBUTE], self.hidden)

    def createBaseImages(self):
        self.compassImage = PILImage.open('Assets/compas.png').resize((self.size, self.size), PILImage.ANTIALIAS)
        self.compassTkimage = ImageTk.PhotoImage(self.compassImage)
        self.compassCanvas_obj1 = self.widget.create_image(int(self.size / 2), int(self.size / 2), image=self.compassTkimage)

        self.arrowImage = PILImage.open('Assets/arrow.png')
        self.arrowImage = self.arrowImage.resize((int(self.size * 2.5), int(self.size * 1.25)), PILImage.ANTIALIAS)
        self.arrowTkimage = ImageTk.PhotoImage(self.arrowImage.rotate(0))
        self.canvas_obj = self.widget.create_image(int(self.size / 2), int(self.size / 2), image=self.arrowTkimage)

    def geterateAngledImage(self, angle):
        self.arrowTkimage = ImageTk.PhotoImage(self.arrowImage.rotate(angle))
        self.canvas_obj = self.widget.create_image(int(self.size / 2), int(self.size / 2), image=self.arrowTkimage)

    def updateInfo(self, data):
        self.geterateAngledImage(self.a)
        self.a += 1

    def getXMLStuff(self, item):
        tag = ET.SubElement(item, Constants.WIDGET_NAME)
        tag.set(Constants.TITTLE_ATTRIBUTE, str(self.title))
        tag.set(Constants.X_POS_ATTRIBUTE, str(self.xPos))
        tag.set(Constants.Y_POS_ATTRIBUTE, str(self.yPos))
        tag.set(Constants.HIDDEN_ATTRIBUTE, str(self.isHidden))
        tag.set(Constants.DRAGGABLE_ATTRIBUTE, str(self.draggable))
        tag.set(Constants.TYPE_ATTRIBUTE, str(self.type))
        tag.set(Constants.SIZE_ATTRIBUTE, str(self.size))


