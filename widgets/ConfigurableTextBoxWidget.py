#!/usr/bin/python

from CustomBaseWidget import *
from Constants import *


class ConfigurableTextBoxWidget(CustomBaseWidget):
    widgetTitle = ""
    configInfo = []

    def __init__(self, configDict):
        title = configDict[Constants.TITTLE_ATTRIBUTE] + "\n"
        tab = configDict[Constants.TAB_ATTRIBUTE]
        font = configDict[Constants.FONT_ATTRIBUTE]
        fontSize = int(configDict[Constants.FONT_SIZE_ATTRIBUTE])
        xpos = configDict[Constants.X_POS_ATTRIBUTE]
        ypos = configDict[Constants.Y_POS_ATTRIBUTE]
        hidden = configDict[Constants.HIDDEN_ATTRIBUTE]
        draggabe = configDict[Constants.DRAGGABLE_ATTRIBUTE]

        self.configInfo = configDict[Constants.CONFIG_ATTRIBUTE]

        self.widgetTitle = title

        self.nameVar = StringVar()
        self.updateInfo(0)

        self.widget = Label(tab, textvariable=self.nameVar, borderwidth=4, relief="raised", font=(font, fontSize))
        self.widget.grid(column=0, row=0)
        self.widget.place(x=xpos, y=ypos)

        CustomBaseWidget.__init__(self, self.widget, draggabe, xpos, ypos)

        self.makeDraggable()
        if(hidden):
            self.hide()
        self.show()

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
