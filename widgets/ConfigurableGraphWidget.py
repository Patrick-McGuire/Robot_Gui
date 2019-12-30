#!/usr/bin/python

import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from CustomBaseWidget import *
from Constants import *

import math, time


class ConfigurableGraphWidget(CustomBaseWidget):
    widgetTitle = ""
    configInfo = []
    xList = []
    yList = []

    def __init__(self, configDict, window):
        self.window = window

        self.title = configDict[Constants.TITTLE_ATTRIBUTE]
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

        # self.configInfo = configDict[Constants.CONFIG_ATTRIBUTE]

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, master=tab)
        self.widget = self.canvas.get_tk_widget()
        self.widget.grid(column=xpos, row=ypos)

        # self.widget.place(x=self.xpos, y=self.ypos)

        CustomBaseWidget.__init__(self, self.widget, draggable, xpos, ypos, window, self.title, hidden)

    def updateInfo(self, data):
        try:
            value = data["batteryVoltage"]
        except:
            return

        self.xList.append(time.time())
        self.yList.append(value)

        if len(self.xList) >= 100:
            self.xList.pop(0)
            self.yList.pop(0)

        self.plot.clear()
        self.plot.plot(self.xList, self.yList)

        self.canvas.show()
