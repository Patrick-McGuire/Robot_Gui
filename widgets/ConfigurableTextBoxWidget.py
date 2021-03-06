#!/usr/bin/python

import xml.etree.ElementTree as ET

from Constants import *
from CustomBaseWidget import *


class ConfigurableTextBoxWidget(CustomBaseWidget):
    def __init__(self, configDict, window):
        self.configInfo = []
        self.type = Constants.CONFIGURABLE_TEXT_BOX_TYPE

        self.window = window
        self.title = configDict[Constants.TITTLE_ATTRIBUTE]
        self.tab = configDict[Constants.TAB_ATTRIBUTE]
        self.font = configDict[Constants.FONT_ATTRIBUTE]
        self.fontSize = int(configDict[Constants.FONT_SIZE_ATTRIBUTE])
        self.xPos = configDict[Constants.X_POS_ATTRIBUTE]
        self.yPos = configDict[Constants.Y_POS_ATTRIBUTE]
        self.hidden = configDict[Constants.HIDDEN_ATTRIBUTE]
        self.draggable = configDict[Constants.DRAGGABLE_ATTRIBUTE]
        self.foregroundColor = configDict[Constants.FOREGROUND_ATTRIBUTE]
        self.backgroundColor = configDict[Constants.BACKGROUND_ATTRIBUTE]
        self.borderWidth = int(configDict[Constants.BORDER_WIDTH_ATTRIBUTE])
        self.relief = configDict[Constants.RELIEF_ATTRIBUTE]

        self.configInfo = configDict[Constants.CONFIG_ATTRIBUTE]

        self.nameVar = StringVar()
        self.updateInfo(0)

        self.widget = Label(self.tab, textvariable=self.nameVar, borderwidth=self.borderWidth, relief=self.relief, background=self.backgroundColor, foreground=self.foregroundColor, font=(self.font, self.fontSize))
        self.widget.grid(column=0, row=0)
        self.widget.place(x=self.xPos, y=self.yPos)
        CustomBaseWidget.__init__(self, self.widget, self.draggable, self.xPos, self.yPos, window, configDict[Constants.TITTLE_ATTRIBUTE], self.hidden)

    def updateInfo(self, data):
        string = self.title

        for i in range(len(self.configInfo)):
            string += "\n"

            if data == 0:
                string += " " + self.configInfo[i][0] + "\t" + "No data "
            elif not self.configInfo[i][1] in data:
                string += " " + self.configInfo[i][0] + "\t" + "No data "
            else:
                string += " " + self.configInfo[i][0] + "\t" + str(data[self.configInfo[i][1]]) + " "

        self.nameVar.set(string)

    def getXMLStuff(self, item):
        tag = ET.SubElement(item, Constants.WIDGET_NAME)
        tag.set(Constants.TITTLE_ATTRIBUTE, str(self.title))
        tag.set(Constants.X_POS_ATTRIBUTE, str(self.xPos))
        tag.set(Constants.Y_POS_ATTRIBUTE, str(self.yPos))
        tag.set(Constants.FONT_ATTRIBUTE, str(self.font))
        tag.set(Constants.FONT_SIZE_ATTRIBUTE, str(self.fontSize))
        tag.set(Constants.BACKGROUND_ATTRIBUTE, str(self.backgroundColor))
        tag.set(Constants.FOREGROUND_ATTRIBUTE, str(self.foregroundColor))
        tag.set(Constants.RELIEF_ATTRIBUTE, str(self.relief))
        tag.set(Constants.BORDER_WIDTH_ATTRIBUTE, str(self.borderWidth))
        tag.set(Constants.HIDDEN_ATTRIBUTE, str(self.isHidden))
        tag.set(Constants.DRAGGABLE_ATTRIBUTE, str(self.draggable))
        tag.set(Constants.TYPE_ATTRIBUTE, str(self.type))

        items = []
        for line in self.configInfo:
            items.append(ET.SubElement(tag, Constants.LINE_NAME))
            items[-1].set(Constants.LABEL_ATTRIBUTE, line[0])
            items[-1].set(Constants.VALUE_ATTRIBUTE, line[1])
