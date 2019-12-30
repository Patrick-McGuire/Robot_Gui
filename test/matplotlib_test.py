import matplotlib

matplotlib.use('TkAgg')

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


def test():
    global t, s, canvas, root, f

    t.append(time.time())
    s.append(math.sin(time.time()))

    # print(t)

    if len(t) >= 100:
        t.pop(0)
        s.pop(0)

    a.clear()
    a.plot(t, s)

    canvas.show()

    root.after(10, test)


test()

Tk.mainloop()
