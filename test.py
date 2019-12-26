from Tkinter import *
import cv2
from PIL import Image, ImageTk

def onDragStart(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y


def onDragMotion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)


def makeDraggable(a):
    a.bind("<Button-1>", onDragStart)
    a.bind("<B1-Motion>", onDragMotion)

cap = cv2.VideoCapture(0)

window = Tk()
lmain = Label(window)

makeDraggable(lmain)
lmain.pack()

def show_frame():
    height = 1900
    _, frame = cap.read()
    frame = cv2.resize(frame, (height, int(height * .75)))
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

show_frame()
window.mainloop()
