#!/usr/bin/python
import ttk
from widgets import ConfigurableTextBoxWidget, VideoScreen

class GUIGenerator:
    guiTabs = []
    allWidgetsList = []
    def __init__(self, window):
        self.window = window
        self.tab_control = ttk.Notebook(self.window)

    # Add a tab to the window
    def addTab(self, name):
        self.guiTabs.append(ttk.Frame(self.tab_control))
        self.tab_control.add(self.guiTabs[-1], text=name)

    def initTabs(self):
        self.tab_control.pack(expand=1, fill='both')

    # Set the size the window will be when it is opens
    def setWindowSize(self, w, h):
        self.window.geometry(w + "x" + h)

    # Set the name that the window will be called
    def setWindowName(self, name):
        self.window.title(name)

    def createConfigurableTextBox(self, widgetInfo):
        self.allWidgetsList.append(ConfigurableTextBoxWidget.ConfigurableTextBoxWidget(widgetInfo, self.window))

    def createVideoWindow(self, widgetInfo):
        self.allWidgetsList.append(VideoScreen.VideoScreen(widgetInfo, self.window))

    def getGuiTabs(self):
        return self.guiTabs

    def getAllWidgetsList(self):
        return self.allWidgetsList