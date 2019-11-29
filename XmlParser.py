#!/usr/bin/python
import xml.dom.minidom
import ttk
from Tkinter import *
from ttk import *
from Constants import *
from widgets import ConfigurableTextBoxWidget


class XmlParser:
    windowName = ""
    dataPassDictionary = {}

    def __init__(self, filename, window):
        self.allWidgetsList = []
        self.window = window

        # Turn the file into a xml file
        self.document = xml.dom.minidom.parse(filename)

        # Get the label/value data for every element in the file
        lines = self.document.getElementsByTagName(Constants.LINE_NAME)
        for line in lines:
            value = line.getAttribute(Constants.VALUE_ATTRIBUTE)
            self.dataPassDictionary[value] = 0


        # Get the title from the file
        self.windowName = self.document.getElementsByTagName(Constants.WINDOW_NAME)[0].getAttribute(
            Constants.TITTLE_ATTRIBUTE)

        self.window.title(self.windowName)

        # Stuff
        tabs = self.document.getElementsByTagName(Constants.TAB_NAME)
        self.tab_control = ttk.Notebook(self.window)
        self.guiTabs = []
        i = 0
        for tab in tabs:
            # Generate a tab based on the xml file
            tabName = tab.getAttribute(Constants.TITTLE_ATTRIBUTE)
            self.guiTabs.append(ttk.Frame(self.tab_control))
            self.tab_control.add(self.guiTabs[i], text=tabName)

            # Get a list of widgits for the current tab
            widgets = tab.getElementsByTagName(Constants.WIDGET_NAME)
            for widget in widgets:
                self.createWidget(widget, self.guiTabs[i])
            i += 1

        self.tab_control.pack(expand=1, fill='both')

    def createWidget(self, widget, tab):
        title = widget.getAttribute(Constants.TITTLE_ATTRIBUTE)
        font = widget.getAttribute(Constants.FONT_ATTRIBUTE)
        fontSize = widget.getAttribute(Constants.FONT_SIZE_ATTRIBUTE)
        xpos = widget.getAttribute(Constants.X_POS_ATTRIBUTE)
        ypos = widget.getAttribute(Constants.Y_POS_ATTRIBUTE)
        hidden = widget.getAttribute(Constants.HIDDEN_ATTRIBUTE) == "True"
        draggable = widget.getAttribute(Constants.DRAGGABLE_ATTRIBUTE) == "True"

        widgetInfo = {
            Constants.TITTLE_ATTRIBUTE : title,
            Constants.FONT_ATTRIBUTE : font,
            Constants.TAB_ATTRIBUTE : tab,
            Constants.FONT_SIZE_ATTRIBUTE : fontSize,
            Constants.X_POS_ATTRIBUTE : xpos,
            Constants.Y_POS_ATTRIBUTE : ypos,
            Constants.HIDDEN_ATTRIBUTE : hidden,
            Constants.DRAGGABLE_ATTRIBUTE : draggable
        }

        type = widget.getAttribute(Constants.TYPE_ATTRIBUTE)
        self.configInfo = []
        if (type == Constants.CONFIGURABLE_TEXT_BOX):
            lines = widget.getElementsByTagName(Constants.LINE_NAME)
            for line in lines:
                label = line.getAttribute(Constants.LABEL_ATTRIBUTE)
                value = line.getAttribute(Constants.VALUE_ATTRIBUTE)
                self.configInfo.append([label, value])

            widgetInfo[Constants.CONFIG_ATTRIBUTE] = self.configInfo
            self.allWidgetsList.append(ConfigurableTextBoxWidget.ConfigurableTextBoxWidget(widgetInfo))

    def getDataPassDictionary(self):
        return self.dataPassDictionary

    def getAllWidgetsList(self):
        print(self.allWidgetsList)
        return self.allWidgetsList

    def getConfigInfo(self):
        return self.configInfo
