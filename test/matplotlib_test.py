#!/usr/bin/python
import matplotlib
import threading

matplotlib.use('TkAgg')
from multiprocessing import Process, Queue
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import math
import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

t = []
s = []

root = Tk.Tk()

f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)

canvas = FigureCanvasTkAgg(f, master=root)
#canvas.show()
# canvas.get_tk_widget().grid(side=Tk.TOP, fill=Tk.BOTH, expand=1)
canvas.get_tk_widget().grid(column=0, row=0)
widget = canvas.get_tk_widget()

def test(Q, canvassss):
    i = 0
    while True:
        canvassss.get_tk_widget().place(x=i, y=i)
        print 'fds'
        # time.sleep(20)
        i += 1000
        Q.put(canvassss)
    #     t.append(time.time())
    #     s.append(math.sin(time.time()))
    #
    # # print(t)
    #
    #     if len(t) >= 100:
    #         t.pop(0)
    #         s.pop(0)
    #
    #     a.clear()
    #     a.plot(t, s)
    #     try:
    #         canvassss.show()
    #         Q.put(canvassss)
    #     except RuntimeError:
    #         print ("bruh")
    # root.after(10, test)




# test()
# x = threading.Thread(target=test)
# x.start()
q = Queue()
p = Process(target=test, args=(q,canvas))
p.start()

def test1():
    global canvas
    del canvas
    try:
        canvas = q.get()
    except UnpickleableError:
        pass
    root.after(10, test1)
    canvas.update()

root.after(3000, test1)
Tk.mainloop()
