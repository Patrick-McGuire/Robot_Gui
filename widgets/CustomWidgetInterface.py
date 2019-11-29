#!/usr/bin/python

import abc


class WidgetInterface(abc.ABC):
    @abc.abstractmethod
    def updateInfo(self):
        pass
