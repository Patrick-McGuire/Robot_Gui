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

        title = configDict[Constants.TITTLE_ATTRIBUTE]
        tab = configDict[Constants.TAB_ATTRIBUTE]
        font = configDict[Constants.FONT_ATTRIBUTE]
        fontSize = int(configDict[Constants.FONT_SIZE_ATTRIBUTE])
        xpos = configDict[Constants.X_POS_ATTRIBUTE]
        ypos = configDict[Constants.Y_POS_ATTRIBUTE]
        hidden = configDict[Constants.HIDDEN_ATTRIBUTE]
        draggable = configDict[Constants.DRAGGABLE_ATTRIBUTE]
        foregroundColor = configDict[Constants.FOREGROUND_ATTRIBUTE]
        backgroundColor = configDict[Constants.BACKGROUND_ATTRIBUTE]
        borderwidth = int(configDict[Constants.BORDER_WIDTH_ATTRIBUTE])
        relief = configDict[Constants.RELIEF_ATTRIBUTE]

        config = configDict["config"]
        self.videoStream = config[0]
        self.width, self.height = config[1].split("x")
        self.fullScreen = config[2]
        self.lockAspectRatio = config[3]

        if self.fullScreen:
            static = True
        else:
            static = False

        self.configInfo = configDict[Constants.CONFIG_ATTRIBUTE]

        self.widgetTitle = title + "\n"

        self.nameVar = StringVar()
        self.updateInfo(0)

        self.widget = Label(tab)
        self.widget.grid(column=0, row=0)
        self.widget.place(x=xpos, y=ypos)

        CustomBaseWidget.__init__(self, self.widget, draggable, xpos, ypos, window, title, static=static)

        self.makeDraggable()
        if hidden:
            self.hide()

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
        aspectRatio = float(width)/float(height)

        print(aspectRatio)

        if self.fullScreen:
            self.width = self.window.winfo_width()
            self.height = self.window.winfo_height()

        frame = cv2.resize(frame, (int(self.width), int(self.height)))
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.widget.imgtk = imgtk
        self.widget.configure(image=imgtk)
