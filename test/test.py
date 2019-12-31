#!/usr/bin/python
import Tkinter
from PIL import ImageTk
from PIL import Image as Image2
from Tkinter import *

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

root = Tkinter.Tk()
canvas = Canvas(root, width=600, height=600, bg="Black")
# canvas.create_oval(0,0,600,600, fill="Black")

make_draggable(canvas)
canvas.grid(column=0, row=0)

image1 = Image2.open('Assets/compass.png').resize((600, 600), Image2.ANTIALIAS)
tkimage1 = ImageTk.PhotoImage(image1)
canvas_obj1 = canvas.create_image(300, 300, image=tkimage1)

angle = 0
image = Image2.open('Assets/arrow.png')
image = image.resize((int(1000 * 1.5), int(500 * 1.5)), Image2.ANTIALIAS)
tkimage = ImageTk.PhotoImage(image.rotate(angle))
canvas_obj = canvas.create_image(300, 300, image=tkimage)

def draw():
    global angle, image, tkimage, canvas_obj
    # canvas.delete(canvas_obj)

    tkimage = ImageTk.PhotoImage(image.rotate(angle))
    canvas_obj = canvas.create_image(300, 300, image=tkimage)

    # canvas.update()
    angle += 0.1
    # angle %= 360
    root.after(10,draw)

root.after(100, draw)
root.mainloop()
