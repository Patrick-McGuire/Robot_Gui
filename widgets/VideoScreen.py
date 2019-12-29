#!/usr/bin/python

from CustomBaseWidget import *
from Constants import *
import cv2
from PIL import Image, ImageTk
import xml.etree.ElementTree as ET


class VideoScreen(CustomBaseWidget):
    widgetTitle = ""
    configInfo = []
    hasVideoStream = False
    type = Constants.VIDEO_WINDOW_TYPE

    def __init__(self, configDict, window):
        self.window = window

        self.title = configDict[Constants.TITTLE_ATTRIBUTE]
        self.tab = configDict[Constants.TAB_ATTRIBUTE]
        self.xpos = configDict[Constants.X_POS_ATTRIBUTE]
        self.ypos = configDict[Constants.Y_POS_ATTRIBUTE]
        self.hidden = configDict[Constants.HIDDEN_ATTRIBUTE]
        self.draggable = configDict[Constants.DRAGGABLE_ATTRIBUTE]

        self.videoStream = configDict[Constants.SOURCE_ATTRIBUTE]
        self.width, self.height = configDict[Constants.DIMENSIONS_ATTRIBUTE].split("x")
        self.fullScreen = configDict[Constants.FULLSCREEN_ATTRIBUTE] == "True"
        self.lockAspectRatio = configDict[Constants.LOCK_ASPECT_RATIO_ATTRIBUTE] == "True"

        if self.fullScreen:
            static = True
        else:
            static = False

        self.widgetTitle = self.title + "\n"

        self.nameVar = StringVar()
        self.updateInfo(0)

        self.widget = Label(self.tab)
        self.widget.grid(column=0, row=0)
        self.widget.place(x=self.xpos, y=self.ypos)
        CustomBaseWidget.__init__(self, self.widget, self.draggable, self.xpos, self.ypos, self.window, self.title, self.hidden, static)

    def setDimensions(self, width, height):
        self.width = width
        self.height = height

    def updateInfo(self, data):
        if data != 0:
            frame = data[self.videoStream]
            # Check if we are actually sent an image
            if str(frame) == "0":
                pass
            else:
                self.hasVideoStream = True
                self.displayImage(frame)

    def displayImage(self, frame):
        height, width, channels = frame.shape
        aspectRatio = float(width) / float(height)

        windowHeight = float(self.window.winfo_height())
        windowWidth = float(self.window.winfo_width())
        windowAspectRatio = windowWidth / windowHeight
        if self.fullScreen:
            self.width = windowWidth
            self.height = windowHeight

            if self.lockAspectRatio:
                if aspectRatio >= windowAspectRatio:
                    self.width = windowWidth
                    self.height = windowWidth / aspectRatio
                    self.yPos = ((windowHeight - self.height) / 2)
                    self.xPos = 0
                else:
                    self.height = windowHeight
                    self.width = windowHeight * aspectRatio
                    self.xPos = (windowWidth - self.width) / 2
                    self.yPos = 0

                self.widget.place(x=self.xPos, y=self.yPos)

        frame = cv2.resize(frame, (int(self.width), int(self.height)))
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        imgtk = ImageTk.PhotoImage(image=Image.fromarray(cv2image))
        self.widget.imgtk = imgtk
        self.widget.configure(image=imgtk)

    def getXMLStuff(self, item):
        tag = ET.SubElement(item, Constants.WIDGET_NAME)
        tag.set(Constants.TITTLE_ATTRIBUTE, str(self.title))
        tag.set(Constants.X_POS_ATTRIBUTE, str(self.xPos))
        tag.set(Constants.Y_POS_ATTRIBUTE, str(self.yPos))
        tag.set(Constants.HIDDEN_ATTRIBUTE, str(self.isHidden))
        tag.set(Constants.DRAGGABLE_ATTRIBUTE, str(self.draggable))
        tag.set(Constants.TYPE_ATTRIBUTE, str(self.type))

        tag.set(Constants.SOURCE_ATTRIBUTE, str(self.videoStream))
        tag.set(Constants.DIMENSIONS_ATTRIBUTE, str(self.width) + "x" + str(self.height))
        tag.set(Constants.FULLSCREEN_ATTRIBUTE, str(self.fullScreen))
        tag.set(Constants.LOCK_ASPECT_RATIO_ATTRIBUTE, str(self.lockAspectRatio))