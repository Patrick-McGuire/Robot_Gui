#!/usr/bin/python

from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk(  )

#This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")


Title = root.title( "File Opener")
label = ttk.Label(root, text ="I'm BATMAN!!!",foreground="red",font=("Helvetica", 16))
label.pack()

#Menu Bar

menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)

file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = lambda:exit())

menu.add_cascade(label = 'File', menu = file)





root.mainloop()