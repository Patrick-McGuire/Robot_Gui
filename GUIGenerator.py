#!/usr/bin/python
import ttk
from widgets import SpinnyCompassWidget
from widgets import ConfigurableTextBoxWidget, VideoScreen, VilibilityToggleCheckBoxWidget, ConfigurableGraphWidget
from Tkinter import *
from XMLOutput import XMLOutput
import tkFileDialog


class GUIGenerator:
    globalLockedState = True
    guiTabs = []
    allWidgetsList = []
    menueList = []

    def __init__(self, window, filePath):
        self.window = window
        self.tab_control = ttk.Notebook(self.window)

        self.filePath = filePath
        self.shortFilePath = list(self.filePath)
        for i in range(len(self.shortFilePath) - 1, 0, -1):
            if (self.shortFilePath.pop(i) == "/"):
                break
        self.shortFilePath = "".join(self.shortFilePath)

    # Add all of the basic features for operation
    def preInit(self):
        self.addTab("Settings")

    def postInit(self):
        # Settings tab stuff
        for i in range(len(self.allWidgetsList)):
            self.allWidgetsList.append(
                VilibilityToggleCheckBoxWidget.VilibilityToggleCheckBoxWidget(self.guiTabs[0], [10, 10 + (20 * i)],
                                                                              self.window,
                                                                              self.allWidgetsList[i].widgetTittle,
                                                                              self.allWidgetsList[i], i))
            self.allWidgetsList[i].setHidderWidget(self.allWidgetsList[-1])
            self.allWidgetsList[i].setAllWidsList(self.allWidgetsList)

        # Menu stuff
        basicMenue = [["Lock All Widgets", self.lockAllWidgets], ["Unlock All Widgets", self.unlockAllWidgets],
                      ["Enable Hide On Click", self.hideOnClick], ["Disable Hide On Click", self.disableOnClick],
                      ["Show All Widgets", self.showAllWidgets]]
        saveMenue = [["Save as", self.saveAs], ["Save", self.save]]
        menueNames = ["File", "Settings"]
        self.newMenu(menueNames, [saveMenue, basicMenue])

        # Key binds
        self.window.bind('<Escape>', self.disableOnClick)
        self.window.bind('<grave>', self.hideOnClick)
        self.window.bind('<F1>', self.toggleLockAllWidgets)
        self.window.bind('<Control-s>', self.save)
        self.window.bind('<Control-Shift-S>', self.saveAs)

    def newMenu(self, name, options):
        menu = Menu(self.window)
        menuItems = []
        for j in range(len(options)):
            menuItems.append(Menu(menu, tearoff=0))
            for i in options[j]:
                menuItems[-1].add_command(label=i[0], command=i[1])
            menu.add_cascade(label=name[j], menu=menuItems[-1])

        self.window.config(menu=menu)

    # Add a tab to the window
    def addTab(self, name):
        self.guiTabs.append(ttk.Frame(self.tab_control))
        self.tab_control.add(self.guiTabs[-1], text=name)

    def initTabs(self):
        # self.tab_control.grid(column=0, row=0)
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

    def createCompass(self, widgetInfo):
        self.allWidgetsList.append(SpinnyCompassWidget.SpinnyCompassWidget(widgetInfo, self.window))

    def createConfigurableGraph(self, widgetInfo):
        self.allWidgetsList.append(ConfigurableGraphWidget.ConfigurableGraphWidget(widgetInfo, self.window))

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

    def toggleLockAllWidgets(self, e=0):
        if self.globalLockedState:
            for widget in self.allWidgetsList:
                widget.dragOff()
        else:
            for widget in self.allWidgetsList:
                widget.dragOn()
        self.globalLockedState = not self.globalLockedState

    def showAllWidgets(self):
        for widget in self.allWidgetsList:
            widget.show()

    def hideOnClick(self, e=0):
        for widget in self.allWidgetsList:
            widget.hideOnClick = True

    def disableOnClick(self, e=0):
        for widget in self.allWidgetsList:
            widget.hideOnClick = False

    def setParser(self, parser):
        self.parser = parser

    def saveAs(self, e=0):
        filename = tkFileDialog.asksaveasfilename(initialdir=self.shortFilePath, title="Select file",
                                                  filetypes=(("xml files", "*.xml"), ("all files", "*.*")))
        if (type(filename) == type("") and filename != ""):
            self.saveXML(filename)

    def save(self, e=0):
        self.saveXML(self.filePath)

    def saveXML(self, filepathy):
        windoInfo = [self.parser.getGuiName(), self.window.winfo_width(), self.window.winfo_height()]
        tabData = self.parser.getTabInfo()
        widgetsByTab = self.parser.getWidgesByTab()
        XMLOutput(windoInfo, tabData, widgetsByTab, self.filePath)
