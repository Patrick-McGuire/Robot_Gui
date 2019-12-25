#!/usr/bin/python

from CustomBaseWidget import *
from Constants import *


class ConfigurableTextBoxWidget(CustomBaseWidget):
    widgetTitle = ""
    configInfo = []

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

        self.widget = Label(tab, textvariable=self.nameVar, borderwidth=borderwidth, relief=relief, background=backgroundColor, foreground=foregroundColor, font=(font, fontSize))
        self.widget.grid(column=0, row=0)
        self.widget.place(x=xpos, y=ypos)

        CustomBaseWidget.__init__(self, self.widget, draggabe, xpos, ypos, window)

        self.makeDraggable()
        if(hidden):
            self.hide()


    def updateInfo(self, data):
        string = self.widgetTitle + "\n"

        for i in range(len(self.configInfo)):
            if data == 0:
                string += " " + self.configInfo[i][0] + "\t" + "No data "
            elif len(data) == 0:
                string += " " + self.configInfo[i][0] + "\t" + "No data "
            else:
                string += " " + self.configInfo[i][0] + "\t" + str(data[self.configInfo[i][1]]) + " "

            string += "\n"

        self.nameVar.set(string)

