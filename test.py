#!/usr/bin/python
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
root.filename = tkFileDialog.asksaveasfilename(initialdir="/", title="Select file",
                                               filetypes=(("xml files", "*.xml"), ("all files", "*.*")))
print (root.filename)
# root.mainloop()