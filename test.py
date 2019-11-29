#!/usr/bin/python

import ttk
from Tkinter import *
from ttk import *
import random


def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)





testText = '''
 Battery Voltage: 
 Current Draw: 
 5v Bus: 
 3.3v Bus: 
'''
window = Tk()
window.title("Test App ")
window.geometry('1920x1080')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Tab 1')
tab_control.add(tab2, text='Tab 2')
a = StringVar()
a.set("Hi")
lbl1 = Label(tab1, textvariable=a, borderwidth = 4, relief="raised", font=("Arial", 20))
lbl1.grid(column=0, row=0)
lbl1.place(x = 40, y = 50)
make_draggable(lbl1)
lbl2 = Label(tab2, text='label2')

lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')


def updateVoltage():
    batteryVoltage = random.randint(0, 10)
    currentDraw = random.randint(0, 10)
    bus5v = random.randint(0, 10)
    bus33v = random.randint(0, 10)

    testText = '''                                 
 Battery Voltage: {0} 
 Current Draw: {1} 
 5v Bus: {2} 
 3.3v Bus: {3} 
 '''.format(batteryVoltage, currentDraw, bus5v, bus33v)
    a.set(testText)
    window.after(100, updateVoltage)


window.after(100, updateVoltage)

window.mainloop()


