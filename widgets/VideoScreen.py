#!/usr/bin/python

from CustomBaseWidget import *
from Constants import *
import cv2
from PIL import Image, ImageTk


class VideoScreen(CustomBaseWidget):
    widgetTitle = ""
    configInfo = []
    hasVideoStream = False

    def __init__(self, configDict, window):
        self.window = window

        title = configDict[Constants.TITTLE_ATTRIBUTE] + "\n"
        tab = configDict[Constants.TAB_ATTRIBUTE]
        font = configDict[Constants.FONT_ATTRIBUTE]
        fontSize = int(configDict[Constants.FONT_SIZE_ATTRIBUTE])
        xpos = configDict[Constants.X_POS_ATTRIBUTE]
        ypos = configDict[Constants.Y_POS_ATTRIBUTE]
        hidden = configDict[Constants.HIDDEN_ATTRIBUTE]
        draggabe = configDict[Constants.DRAGGABLE_ATTRIBUTE]
        foregroundColor = configDict[Constants.FOREGROUND_ATTRIBUTE]
        backgroundColor = configDict[Constants.BACKGROUND_ATTRIBUTE]
        borderwidth = int(configDict[Constants.BORDER_WIDTH_ATTRIBUTE])
        relief = configDict[Constants.RELIEF_ATTRIBUTE]

        self.configInfo = configDict[Constants.CONFIG_ATTRIBUTE]

        self.widgetTitle = title

        self.nameVar = StringVar()
        self.updateInfo(0)

        self.widget = Label(tab)
        self.widget.grid(column=0, row=0)
        self.widget.place(x=xpos, y=ypos)

        CustomBaseWidget.__init__(self, self.widget, draggabe, xpos, ypos, window)

        self.cap = cv2.VideoCapture(0)
        self.hasVideoStream = True

        self.makeDraggable()
        if (hidden):
            self.hide()

    def updateInfo(self, data):
        if self.hasVideoStream:
            self.readStream(data)

    def readStream(self, data):
        height = 1000
        _, frame = self.cap.read()
        frame = cv2.resize(frame, (height, int(height * .75)))
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.widget.imgtk = imgtk
        self.widget.configure(image=imgtk)
