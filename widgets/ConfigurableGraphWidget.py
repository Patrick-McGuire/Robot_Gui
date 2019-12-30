#!/usr/bin/python

import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from CustomBaseWidget import *
from Constants import *

import time


class ConfigurableGraphWidget(CustomBaseWidget):
    widgetTitle = ""
    configInfo = []
    xList = []
    yList = []
    a = 1

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

        self.configInfo = configDict[Constants.CONFIG_ATTRIBUTE]

        for i in range(len(self.configInfo)):
            self.yList.append([])

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, master=tab)
        self.widget = self.canvas.get_tk_widget()
        self.widget.grid(column=xpos, row=ypos)

        CustomBaseWidget.__init__(self, self.widget, draggable, xpos, ypos, window, self.title, hidden)

    def updateInfo(self, data):
        if not self.configInfo[0][1] in data:
            return

        #Don't create and draw plot in same loop, because its too slow
        if self.a > 0:
            self.createPlot(data)
        else:
            self.drawPlot()
        self.a *= -1

    def createPlot(self, data):
        legend = []
        self.xList.append(time.time())

        if len(self.xList) >= 100:
            self.xList.pop(0)
            overflow = True
        else:
            overflow = False

        self.plot.clear()
        for i in range(len(self.configInfo)):
            value = data[self.configInfo[i][1]]
            legend.append(self.configInfo[i][0])

            self.yList[i].append(value)

            if overflow:
                self.yList[i].pop(0)

            self.plot.set_title(self.title)
            self.plot.plot(self.xList, self.yList[i])

        self.plot.legend(legend, loc='upper left')

    def drawPlot(self):
        self.canvas.show()
