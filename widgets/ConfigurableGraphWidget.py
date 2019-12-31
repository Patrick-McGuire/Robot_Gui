#!/usr/bin/python

import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from CustomBaseWidget import *
from Constants import *
import time


class ConfigurableGraphWidget(CustomBaseWidget):
    def __init__(self, configDict, window):
        self.configInfo = []
        self.xList = []
        self.yList = []
        self.a = 1
        self.data = 0
        self.b = 0

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

        self.startTime = time.time()

        CustomBaseWidget.__init__(self, self.widget, draggable, xpos, ypos, window, self.title, hidden)

    def updateInfo(self, data):
        if not self.configInfo[0][1] in data:
            return

        self.recordData(data)

        if self.b % 2 == 0:
            # Don't create and draw plot in same loop, because its too slow
            if self.a > 0:
                self.createPlot()
            else:
                self.drawPlot()
            self.a *= -1
        self.b += 1

    def recordData(self, data):
        self.xList.append(time.time()-self.startTime)

        if len(self.xList) >= 50:
            self.xList.pop(0)
            overflow = True
        else:
            overflow = False

        for i in range(len(self.configInfo)):
            value = data[self.configInfo[i][1]]

            self.yList[i].append(value)

            if overflow:
                self.yList[i].pop(0)

    def createPlot(self):
        legend = []

        self.plot.clear()
        for i in range(len(self.configInfo)):
            self.plot.set_title(self.title)
            self.plot.plot(self.xList, self.yList[i])

        self.plot.legend(legend, loc='upper left')

    def drawPlot(self):
        self.canvas.show()
