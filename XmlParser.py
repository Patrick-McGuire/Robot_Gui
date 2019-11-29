#!/usr/bin/python
import xml.dom.minidom
import ttk
from Tkinter import *
from ttk import *
from Constants import *

class XmlParser:
    windowName = ""
    dataPassDictionary = {}

    def __init__(self, filename, window):
        # Turn the file into a xml file
        self.document = xml.dom.minidom.parse(filename)

        # Get the label/value data for every element in the file
        lines = self.document.getElementsByTagName(Constants.LINE_NAME)
        for line in lines:
            value = line.getAttribute(Constants.VALUE_ATTRIBUTE)
            self.dataPassDictionary[value] = 0

        # Get the title from the file
        self.windowName = self.document.getElementsByTagName(Constants.WINDOW_NAME)[0].getAttribute(Constants.TITTLE_ATTRIBUTE)

        # Stuff
        tabs = self.document.getElementsByTagName(Constants.TAB_NAME)
        for tab in tabs:
            widgets = tab.getElementsByTagName(Constants.WIDGET_NAME)
            for widget in widgets:
                print(widget.getAttribute(Constants.TITTLE_ATTRIBUTE))
            print("")

    def getDataPassDictionary(self):
        return self.dataPassDictionary


a = XmlParser("config/BasicConfig.xml", "")