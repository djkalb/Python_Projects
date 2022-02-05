
import tkinter
from tkinter import *


root = tkinter.Tk()
f = Frame(root)
b1 = Button(f, text="One")
b1.pack(side=LEFT)
b2 = Button(f, text= "Two")
b2.pack(side=LEFT)
b3 = Button(f, text="three")
b3.pack(side=LEFT)

def but1():
    print("i pushed a thing")
b1.configure(text="Uno", command=but1)



l = Label(root, text="This is a label")
l.pack()
f.pack()






     
root.mainloop()        


