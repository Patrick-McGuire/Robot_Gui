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


        # Get the title and other info from the file
        self.windowName = self.document.getElementsByTagName(Constants.WINDOW_NAME)[0].getAttribute(
            Constants.TITTLE_ATTRIBUTE)
        windowHeight = self.document.getElementsByTagName(Constants.WINDOW_NAME)[0].getAttribute(
             Constants.HEIGHT_ATTRIBUTE)
        windowWidth = self.document.getElementsByTagName(Constants.WINDOW_NAME)[0].getAttribute(
            Constants.WIDTH_ATTRIBUTE)

        self.window.geometry(windowWidth + "x" + windowHeight)
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
        title =           self.getAttribute(widget, Constants.TITTLE_ATTRIBUTE, "Error: no tittle")
        font =            self.getAttribute(widget, Constants.FONT_ATTRIBUTE, "Arial")
        fontSize =        self.getAttribute(widget, Constants.FONT_SIZE_ATTRIBUTE, "20")
        xpos =            self.getAttribute(widget, Constants.X_POS_ATTRIBUTE, "0")
        ypos =            self.getAttribute(widget, Constants.Y_POS_ATTRIBUTE, "0")
        foregroundColor = self.getAttribute(widget, Constants.FOREGROUND_ATTRIBUTE, "Black")
        backgroundColor = self.getAttribute(widget, Constants.BACKGROUND_ATTRIBUTE, "Light Grey")
        hidden =          self.getAttribute(widget, Constants.HIDDEN_ATTRIBUTE, "False") == "True"
        draggable =       self.getAttribute(widget, Constants.DRAGGABLE_ATTRIBUTE, "True") == "True"
        borderwidth =     self.getAttribute(widget, Constants.BORDER_WIDTH_ATTRIBUTE, "4")
        relief =          self.getAttribute(widget, Constants.RELIEF_ATTRIBUTE, "raised")

        widgetInfo = {
            Constants.TITTLE_ATTRIBUTE : title,
            Constants.FONT_ATTRIBUTE : font,
            Constants.TAB_ATTRIBUTE : tab,
            Constants.FONT_SIZE_ATTRIBUTE : fontSize,
            Constants.X_POS_ATTRIBUTE : xpos,
            Constants.Y_POS_ATTRIBUTE : ypos,
            Constants.HIDDEN_ATTRIBUTE : hidden,
            Constants.DRAGGABLE_ATTRIBUTE : draggable,
            Constants.FOREGROUND_ATTRIBUTE : foregroundColor,
            Constants.BACKGROUND_ATTRIBUTE : backgroundColor,
            Constants.BORDER_WIDTH_ATTRIBUTE : borderwidth,
            Constants.RELIEF_ATTRIBUTE : relief
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
            self.allWidgetsList.append(ConfigurableTextBoxWidget.ConfigurableTextBoxWidget(widgetInfo, self.window))

    def getAttribute(self, xmlClip, attribute, defult):
        data = xmlClip.getAttribute(attribute)
        if(data == ""):
            return defult
        return data

    def getDataPassDictionary(self):
        return self.dataPassDictionary

    def getAllWidgetsList(self):
        print(self.allWidgetsList)
        return self.allWidgetsList

    def getConfigInfo(self):
        return self.configInfo
