#!/usr/bin/python

from CustomBaseWidget import *


class ConfigurableTextBoxWidget(CustomBaseWidget):
    widgetTitle = ""
    configInfo = []

    def __init__(self, configDict):
        CustomBaseWidget.__init__(self)

        title = configDict["title"] + "\n"
        tab = configDict["tab"]
        font = configDict["font"]
        xpos = configDict["xPos"]
        ypos = configDict["yPos"]

        self.configInfo = configDict["config"]

        self.widgetTitle = title

        self.nameVar = StringVar()
        self.updateInfo(0)

        self.widget = Label(tab, textvariable=self.nameVar, borderwidth=4, relief="raised", font=(font, 20))
        self.widget.grid(column=0, row=0)
        self.widget.place(x=xpos, y=ypos)
        self.makeDraggable(self.widget)

    def updateInfo(self, data):
        string = self.widgetTitle + "\n"

        for i in range(len(self.configInfo)):
            if data == 0:
                string += self.configInfo[i][0] + "\t" + "No data"
            else:
                string += self.configInfo[i][0] + "\t" + str(data[self.configInfo[i][1]])

            string += "\n"

        self.nameVar.set(string)
