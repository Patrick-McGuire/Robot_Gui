#!/usr/bin/python
import xml.dom.minidom
from Constants import *
from GUIGenerator import GUIGenerator


class XmlParser:
    dataPassDictionary = {}
    widgesByTab = []
    tabData = []
    configInfo = []

    def __init__(self, filename, window):
        self.guiGenerator = GUIGenerator(window, filename)

        self.allWidgetsList = []
        self.window = window

        # Init the gui (add settings tab, do other things)
        self.guiGenerator.preInit()

        # Turn the file into a xml file
        self.document = xml.dom.minidom.parse(filename)

        # Get the keys for the the data pass dictionary, and insert them in to the dict
        lines = self.document.getElementsByTagName(Constants.LINE_NAME)
        for line in lines:
            value = line.getAttribute(Constants.VALUE_ATTRIBUTE)
            self.dataPassDictionary[value] = 0

        # Get attributes that will apply to the entire window
        self.guiName = self.document.getElementsByTagName(Constants.WINDOW_NAME)[0].getAttribute(
            Constants.TITTLE_ATTRIBUTE)
        windowHeight = self.document.getElementsByTagName(Constants.WINDOW_NAME)[0].getAttribute(
            Constants.HEIGHT_ATTRIBUTE)
        windowWidth = self.document.getElementsByTagName(Constants.WINDOW_NAME)[0].getAttribute(
            Constants.WIDTH_ATTRIBUTE)
        self.guiGenerator.setWindowName(self.guiName)
        self.guiGenerator.setWindowSize(windowWidth, windowHeight)

        # Get all of the tabs from the file
        tabs = self.document.getElementsByTagName(Constants.TAB_NAME)

        # Generate all of the tabs
        for i in range(0, len(tabs)):
            # Add a new tab for every tab in the xml file
            tabName = tabs[i].getAttribute(Constants.TITTLE_ATTRIBUTE)
            self.guiGenerator.addTab(tabName)
            self.tabData.append([tabName])
            self.widgesByTab.append([])

            # Get a list of widgets for the current tab
            widgets = tabs[i].getElementsByTagName(Constants.WIDGET_NAME)
            for widget in widgets:
                self.createWidget(widget, self.guiGenerator.getGuiTabs()[i + 1])
                self.widgesByTab[i].append(self.guiGenerator.getAllWidgetsList()[-1])

        self.guiGenerator.postInit()
        self.guiGenerator.initTabs()

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

            widgetInfo[Constants.CONFIG_ATTRIBUTE] = self.configInfo
            self.guiGenerator.createConfigurableTextBox(widgetInfo)
        elif type == Constants.VIDEO_WINDOW_TYPE:
            # lines = widget.getElementsByTagName(Constants.LINE_NAME)
            # for line in lines:
            #     value = line.getAttribute(Constants.VALUE_ATTRIBUTE)
            #     self.configInfo.append(value)
            widgetInfo[Constants.SOURCE_ATTRIBUTE] = self.getAttribute(widget, Constants.SOURCE_ATTRIBUTE, "webcam")
            widgetInfo[Constants.DIMENSIONS_ATTRIBUTE] = self.getAttribute(widget, Constants.DIMENSIONS_ATTRIBUTE, "800x600")
            widgetInfo[Constants.FULLSCREEN_ATTRIBUTE] = self.getAttribute(widget, Constants.FULLSCREEN_ATTRIBUTE, "False")
            widgetInfo[Constants.LOCK_ASPECT_RATIO_ATTRIBUTE] = self.getAttribute(widget, Constants.LOCK_ASPECT_RATIO_ATTRIBUTE, "True")

            # widgetInfo[Constants.CONFIG_ATTRIBUTE] = self.configInfo

            self.guiGenerator.createVideoWindow(widgetInfo)
        elif type == Constants.COMPASS_TYPE:
            widgetInfo[Constants.SIZE_ATTRIBUTE] = self.getAttribute(widget, Constants.SIZE_ATTRIBUTE, "200")
            self.guiGenerator.createCompass(widgetInfo)
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
