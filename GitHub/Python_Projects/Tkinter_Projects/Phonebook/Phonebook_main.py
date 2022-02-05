# Python Ver:                   3.10.0
#
# Author:                       Somebody as yet unnamed and unblamed

# Purpose: make a phonebook to calling people in if that becomes a thing again


from tkinter import *
from tkinter import messagebox     
import tkinter

import Phonebook_GUI
import Phonebook_Func    


class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #master frame configuration
        self.master = master
        self.master.minsize(500, 300) 
        self.master.maxsize(500,300)
        #Phonebook_Func.center_window(self, 500, 300)
        self.master.title("Tkinter Phonebook")
        self.master.configure(bg= "#f0f0f0")
        #detects click in NE corner for red x
        self.master.protocol("WM_DELETE_WINDOW", lambda: Phonebook_Func.ask_quit(self))
        arg = self.master

        #loads the widgets
        Phonebook_GUI.load_gui(self)


if __name__ == "__main__":
    root = tkinter.Tk()  
    App = ParentWindow(root)
    root.mainloop()       


    


    