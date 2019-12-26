#!/usr/bin/python
import ttk
from Tkinter import *
from widgets import ConfigurableTextBoxWidget

class GUIGenerator:
    guiTabs = []
    allWidgetsList = []
    menueList = []
    def __init__(self, window):
        self.window = window
        self.tab_control = ttk.Notebook(self.window)

    # Add all of the basic features for operation
    def preInit(self):
        self.addTab("Settings")

    def postInit(self):
        basicMenue = [["Lock All Widgets", self.lockAllWidgets], ["Unlock All Widgets", self.unlockAllWidgets], ["Toggle Hide On Click", self.hideOnClick], ["Show All Widgets", self.showAllWidgets]]
        self.newMenue("Settings", basicMenue)
        self.window.bind('<Escape>', self.disableOnClick)

    def newMenue(self, name, options):
        menu = Menu(self.window)
        new_item = Menu(menu, tearoff=0)
        for i in options:
            new_item.add_command(label=i[0], command=i[1])
        menu.add_cascade(label=name, menu=new_item)
        self.window.config(menu=menu)

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

    def createWidget(self, widgetInfo):
        self.allWidgetsList.append(ConfigurableTextBoxWidget.ConfigurableTextBoxWidget(widgetInfo, self.window))

    def getGuiTabs(self):
        return self.guiTabs

    def getAllWidgetsList(self):
        return self.allWidgetsList

    def lockAllWidgets(self):
        for widget in self.allWidgetsList:
            widget.dragOff()

    def unlockAllWidgets(self):
        for widget in self.allWidgetsList:
            widget.dragOn()

    def showAllWidgets(self):
        for widget in self.allWidgetsList:
            widget.show()

    def hideOnClick(self):
        for widget in self.allWidgetsList:
            widget.hideOnClick = not widget.hideOnClick

    def disableOnClick(self, e):
        for widget in self.allWidgetsList:
            widget.hideOnClick = False