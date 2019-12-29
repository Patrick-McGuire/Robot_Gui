#!/usr/bin/python

from CustomBaseWidget import *


class VilibilityToggleCheckBoxWidget(CustomBaseWidget):

    def __init__(self, tab, pos, window, text, controledWidget, widgNum):
        self.widgNum = widgNum
        self.window = window
        self.controledWidget = controledWidget
        self.state = BooleanVar()
        self.state.set(True)
        self.widget = Checkbutton(tab, text=text, var=self.state)
        self.widget.grid(column=0, row=0)
        self.widget.place(x=pos[0], y=pos[1])

        CustomBaseWidget.__init__(self, self.widget, True, pos[0], pos[1], window, text, False, True)

    def updateInfo(self, data):
        try:
            windowHeight = self.window.winfo_height() - 70
            row = ((self.widgNum * 20) / windowHeight)
            col = (self.widgNum * 20) % windowHeight
            self.widget.place(x=(row * 200) + 20, y=col + 20)
        except ZeroDivisionError:
            pass

        if(self.state.get() == True):
            self.controledWidget.show()
        else:
            self.controledWidget.hide()

    def setState(self, state):
        self.state.set(state)