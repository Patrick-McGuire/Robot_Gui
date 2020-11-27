#!/usr/bin/python
import xml.dom.minidom

from Constants import *


class XmlParser:
    def __init__(self):
        # Local vars
        self.document = None
        # Data pulled from the file
        self.guiName = ""
        self.tabNames = []
        self.widgetInfo = []

        self.dataPassDict = {}

    def pullWindowInfo(self, document):
        # Get attributes that will apply to the entire window
        self.guiName = document.getElementsByTagName(Constants.WINDOW_NAME)[0].getAttribute(
            Constants.TITTLE_ATTRIBUTE)
        windowHeight = document.getElementsByTagName(Constants.WINDOW_NAME)[0].getAttribute(
            Constants.HEIGHT_ATTRIBUTE)
        windowWidth = document.getElementsByTagName(Constants.WINDOW_NAME)[0].getAttribute(
            Constants.WIDTH_ATTRIBUTE)

    def pullTabInfo(self, document):
        tabs = self.document.getElementsByTagName(Constants.TAB_NAME)  # Get all of the tabs from the xml file
        for tab in tabs:                                  # Loop though all the tabs
            self.tabNames.append(tab.getAttribute(Constants.TITTLE_ATTRIBUTE))   # Add the name to the list
            self.pullWidgetInfo(tab)

    def pullWidgetInfo(self, tab):
        widgets = tab.getElementsByTagName(Constants.WIDGET_NAME)
        for widget in widgets:
            widgetInfo = {
                Constants.TITTLE_ATTRIBUTE: self.getAttribute(widget, Constants.TITTLE_ATTRIBUTE, "Error: no tittle"),
                Constants.FONT_ATTRIBUTE: self.getAttribute(widget, Constants.FONT_ATTRIBUTE, "Arial"),
                Constants.TAB_ATTRIBUTE: tab.getAttribute(Constants.TITTLE_ATTRIBUTE),
                Constants.FONT_SIZE_ATTRIBUTE: self.getAttribute(widget, Constants.FONT_SIZE_ATTRIBUTE, "20"),
                Constants.X_POS_ATTRIBUTE: self.getAttribute(widget, Constants.X_POS_ATTRIBUTE, "0"),
                Constants.Y_POS_ATTRIBUTE: self.getAttribute(widget, Constants.Y_POS_ATTRIBUTE, "0"),
                Constants.HIDDEN_ATTRIBUTE: self.getAttribute(widget, Constants.HIDDEN_ATTRIBUTE, "False") == "True",
                Constants.DRAGGABLE_ATTRIBUTE: self.getAttribute(widget, Constants.DRAGGABLE_ATTRIBUTE, "True") == "True",
                Constants.FOREGROUND_ATTRIBUTE: self.getAttribute(widget, Constants.FOREGROUND_ATTRIBUTE, "Black"),
                Constants.BACKGROUND_ATTRIBUTE: self.getAttribute(widget, Constants.BACKGROUND_ATTRIBUTE, "Light Grey"),
                Constants.BORDER_WIDTH_ATTRIBUTE: self.getAttribute(widget, Constants.BORDER_WIDTH_ATTRIBUTE, "4"),
                Constants.RELIEF_ATTRIBUTE: self.getAttribute(widget, Constants.RELIEF_ATTRIBUTE, "raised")
            }


    def parse(self, filename):
        # Parse the XML file
        self.document = xml.dom.minidom.parse(filename)            # Turn the file into a xml file
        self.pullWindowInfo(self.document)                         # Get attributes for the entire window
        self.pullTabInfo(self.document)                            # Get all of the name of tabs

    def createWidget(self, widget, tab):
        title = self.getAttribute(widget, Constants.TITTLE_ATTRIBUTE, "Error: no tittle")
        font = self.getAttribute(widget, Constants.FONT_ATTRIBUTE, "Arial")
        fontSize = self.getAttribute(widget, Constants.FONT_SIZE_ATTRIBUTE, "20")
        xpos = self.getAttribute(widget, Constants.X_POS_ATTRIBUTE, "0")
        ypos = self.getAttribute(widget, Constants.Y_POS_ATTRIBUTE, "0")
        foregroundColor = self.getAttribute(widget, Constants.FOREGROUND_ATTRIBUTE, "Black")
        backgroundColor = self.getAttribute(widget, Constants.BACKGROUND_ATTRIBUTE, "Light Grey")
        hidden = self.getAttribute(widget, Constants.HIDDEN_ATTRIBUTE, "False") == "True"
        draggable = self.getAttribute(widget, Constants.DRAGGABLE_ATTRIBUTE, "True") == "True"
        borderwidth = self.getAttribute(widget, Constants.BORDER_WIDTH_ATTRIBUTE, "4")
        relief = self.getAttribute(widget, Constants.RELIEF_ATTRIBUTE, "raised")

        widgetInfo = {
            Constants.TITTLE_ATTRIBUTE: title,
            Constants.FONT_ATTRIBUTE: font,
            Constants.TAB_ATTRIBUTE: tab,
            Constants.FONT_SIZE_ATTRIBUTE: fontSize,
            Constants.X_POS_ATTRIBUTE: xpos,
            Constants.Y_POS_ATTRIBUTE: ypos,
            Constants.HIDDEN_ATTRIBUTE: hidden,
            Constants.DRAGGABLE_ATTRIBUTE: draggable,
            Constants.FOREGROUND_ATTRIBUTE: foregroundColor,
            Constants.BACKGROUND_ATTRIBUTE: backgroundColor,
            Constants.BORDER_WIDTH_ATTRIBUTE: borderwidth,
            Constants.RELIEF_ATTRIBUTE: relief
        }

        # Code to handle specific types of widgets
        self.configInfo = []
        type = widget.getAttribute(Constants.TYPE_ATTRIBUTE)
        if type == Constants.CONFIGURABLE_TEXT_BOX_TYPE:
            lines = widget.getElementsByTagName(Constants.LINE_NAME)
            for line in lines:
                label = line.getAttribute(Constants.LABEL_ATTRIBUTE)
                value = line.getAttribute(Constants.VALUE_ATTRIBUTE)
                self.configInfo.append([label, value])

                self.dataPassDictionary[value] = 0

            widgetInfo[Constants.CONFIG_ATTRIBUTE] = self.configInfo
            self.guiGenerator.createConfigurableTextBox(widgetInfo)
        elif type == Constants.VIDEO_WINDOW_TYPE:
            widgetInfo[Constants.SOURCE_ATTRIBUTE] = self.getAttribute(widget, Constants.SOURCE_ATTRIBUTE, "webcam")
            widgetInfo[Constants.DIMENSIONS_ATTRIBUTE] = self.getAttribute(widget, Constants.DIMENSIONS_ATTRIBUTE,
                                                                           "800x600")
            widgetInfo[Constants.FULLSCREEN_ATTRIBUTE] = self.getAttribute(widget, Constants.FULLSCREEN_ATTRIBUTE,
                                                                           "False")
            widgetInfo[Constants.LOCK_ASPECT_RATIO_ATTRIBUTE] = self.getAttribute(widget,
                                                                                  Constants.LOCK_ASPECT_RATIO_ATTRIBUTE,
                                                                                  "True")

            # Define data pass values needed
            self.dataPassDictionary[widgetInfo[Constants.SOURCE_ATTRIBUTE]] = 0

            self.guiGenerator.createVideoWindow(widgetInfo)
        elif type == Constants.COMPASS_TYPE:
            widgetInfo[Constants.SIZE_ATTRIBUTE] = self.getAttribute(widget, Constants.SIZE_ATTRIBUTE, "200")
            widgetInfo[Constants.SOURCE_ATTRIBUTE] = self.getAttribute(widget, Constants.SOURCE_ATTRIBUTE, "bruh")
            self.dataPassDictionary[widgetInfo[Constants.SOURCE_ATTRIBUTE]] = 0
            self.guiGenerator.createCompass(widgetInfo)
        elif type == "ConfigurableGraph":
            lines = widget.getElementsByTagName(Constants.LINE_NAME)
            for line in lines:
                label = line.getAttribute(Constants.LABEL_ATTRIBUTE)
                value = line.getAttribute(Constants.VALUE_ATTRIBUTE)
                self.configInfo.append([label, value])

                self.dataPassDictionary[value] = 0

            widgetInfo[Constants.CONFIG_ATTRIBUTE] = self.configInfo
            self.guiGenerator.createConfigurableGraph(widgetInfo)
        else:
            print("Could not create widget {0}: type {1} not supported".format(title, type))

    def getAttribute(self, xmlClip, attribute, default):
        data = xmlClip.getAttribute(attribute)
        if data == "":
            return default
        return data

    def getDataPassDictionary(self):
        return self.dataPassDictionary

    def getAllWidgetsList(self):
        return self.guiGenerator.getAllWidgetsList()

    def getConfigInfo(self):
        return self.configInfo

    def getGuiName(self):
        return self.guiName

    def getTabInfo(self):
        return self.tabData

    def getWidgesByTab(self):
        return self.widgesByTab
