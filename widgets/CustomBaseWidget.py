#!/usr/bin/python

from Tkinter import *


class CustomBaseWidget:
    def __init__(self, widget, draggable, xPos, yPos, window, tittle, hidden, static=False):
        self.toggle = False
        self.toggleTracker = False
        self.hideOnClick = False
        self.widgetTittle = ""
        self.isHidden = False

        self.window = window
        self.widget = widget
        self.draggable = draggable
        self.xPos = xPos
        self.yPos = yPos
        self.static = static
        self.widgetTittle = tittle
        self.hidden = hidden

        self.makeDraggable()

    def makeDraggable(self):
        if not self.static:
            self.widget.bind("<Button-1>", self.onDragStart)
            self.widget.bind("<B1-Motion>", self.onDragMotion)
            # self.widget.bind("<Motion>", self.onDragMotion)
            self.widget.bind("<ButtonRelease-1>", self.onDragEnd)

    def onDragStart(self, event):
        if self.hideOnClick:
            self.hide()
        elif self.draggable:
            # self.widget.lift()
            Misc.lift(self.widget, aboveThis=None)
            self.toggle = not self.toggle
            if self.draggable:
                widget = event.widget
                widget._drag_start_x = event.x
                widget._drag_start_y = event.y

    def onDragMotion(self, event):
        try:
            if self.draggable:
                widget = event.widget
                x = widget.winfo_x() - widget._drag_start_x + event.x
                y = widget.winfo_y() - widget._drag_start_y + event.y

                if x > self.window.winfo_width() - self.widget.winfo_width():
                    x = self.window.winfo_width() - self.widget.winfo_width()
                if x < 0:
                    x = 0
                if y > self.window.winfo_height() - self.widget.winfo_height() - 25:
                    y = self.window.winfo_height() - self.widget.winfo_height() - 25
                if y < 0:
                    y = 0

                self.xPos = x
                self.yPos = y
                widget.place(x=x, y=y)
        except AttributeError:
            pass

    def onDragEnd(self, event):
        if self.draggable:
            try:
                Misc.lower(self.widget, belowThis=self.allWidgetsList[self.widgetIndex + 1].widget)
                # self.widget.lower(self.allWidgetsList[self.widgetIndex + 1].widget)
            except TclError:
                pass
            try:
                del self.widget._drag_start_x
                del self.widget._drag_start_y
            except AttributeError:
                pass

    def hide(self):
        if not self.static and not self.isHidden:
            self.widget.place_forget()
            self.hiddenWidget.setState(False)
            self.isHidden = True

    def show(self):
        if not self.static and self.isHidden:
            self.widget.grid()
            self.widget.place(x=self.xPos, y=self.yPos)
            self.hiddenWidget.setState(True)
            self.isHidden = False

    def dragOn(self):
        self.draggable = True

    def dragOff(self):
        self.draggable = False

    def setHiddenWidget(self, hiddenWidget):
        self.hiddenWidget = hiddenWidget
        if self.hidden:
            self.hide()

    def setAllWidgetsList(self, allWidgetsList):
        self.allWidgetsList = allWidgetsList
        self.widgetIndex = 0
        for i in range(len(self.allWidgetsList)):
            if self.allWidgetsList[i].widget == self.widget:
                self.widgetIndex = i
                break
