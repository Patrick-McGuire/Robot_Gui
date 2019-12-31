# graph.py
# class to show a moving graph
# written by Roger Woollett

from sys import version_info

if version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk


class Trace():
    # class to represent a single trace in a ScrollGraph
    def __init__(self, master, max_x, min_x, colour, size):

        self.master = master
        self.size = size
        self.scale = master.height / (max_x - min_x)
        self.offset = -self.scale * min_x

        # create a list of line ids
        self.lines = list()
        i = 0
        while i < master.width:
            self.lines.append(master.create_line(i, 0, i, 0, fill=colour, width=size))
            i += 1

    def scroll(self, value):
        # scroll to the right and add new value
        value = self.scale * value + self.offset

        # we want positive upwards
        value = self.master.height - value

        # do scroll
        coords = self.master.coords
        i = self.master.width - 1
        while i > 0:
            x = coords(self.lines[i - 1])
            coords(self.lines[i], i, x[1], i, x[3])
            i -= 1

        # add new value
        coords(self.lines[0], 0, value, 0, value + self.size)


class ScrollGraph(tk.Canvas):
    # class to show a scrolling graph
    def __init__(self, master, *args, **kwargs):
        tk.Canvas.__init__(self, master, *args, **kwargs)

        self.width = int(self['width'])
        self.height = int(self['height'])

        self.traces = dict()

    def add_trace(self, name, max_x, min_x, colour='black', size=1):
        # call to add a trace to the graph
        self.traces[name] = Trace(self, max_x, min_x, colour=colour, size=size)

    def scroll(self, name, value):
        # call to add a new value to a trace
        self.traces[name].scroll(value)


class XAxis(tk.Canvas):
    # class to show horizantal x axis with ticks
    def __init__(self, master, big, small, size=1, *args, **kwargs):
        tk.Canvas.__init__(self, master, *args, **kwargs)

        width = int(self['width'])
        height = int(self['height'])

        self.create_line(0, 1, width - 1, 1, width=size)

        # do small ticks
        i = small
        while i < width:
            self.create_line(i, 1, i, height / 2, width=size)
            i += small

        # do big ticks
        i = 0
        while i < width:
            self.create_line(i, 1, i, height, width=size)
            i += big