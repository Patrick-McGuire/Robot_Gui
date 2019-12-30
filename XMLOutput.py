#!/usr/bin/python
import xml.etree.ElementTree as ET
from xml.dom import minidom
from xml.etree import ElementTree

from Constants import *


class XMLOutput:
    def __init__(self, windowInfo, tabInfo, widgetsByTab, filename):
        self.windowInfo = windowInfo
        self.tabInfo = tabInfo
        self.widgetsByTab = widgetsByTab

        self.getWindowStartTag()
        self.getTabTags()

        myfile = open(filename, "w")
        myfile.write(self.prettify(self.fileData))

    def getWindowStartTag(self):
        self.guiName = self.windowInfo[0]
        self.guiSize = [str(self.windowInfo[1]), str(self.windowInfo[2])]

        self.fileData = ET.Element(Constants.WINDOW_NAME)
        self.fileData.set(Constants.TITTLE_ATTRIBUTE, self.guiName)
        self.fileData.set(Constants.WIDTH_ATTRIBUTE, self.guiSize[0])
        self.fileData.set(Constants.HEIGHT_ATTRIBUTE, self.guiSize[1])

    def getTabTags(self):
        items = []
        for i in range(len(self.tabInfo)):
            items.append(ET.SubElement(self.fileData, Constants.TAB_NAME))
            items[-1].set(Constants.TITTLE_ATTRIBUTE, self.tabInfo[i][0])
            for j in range(len(self.widgetsByTab[i])):
                try:
                    self.widgetsByTab[i][j].getXMLStuff(items[-1])
                except AttributeError as e:
                    print(e)
                    print("Can't save {0}: no xml output method".format(self.widgetsByTab[i][j].widgetTittle))

    # make pretty!!
    def prettify(self, elem):
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return str(reparsed.toprettyxml(indent="\t"))
