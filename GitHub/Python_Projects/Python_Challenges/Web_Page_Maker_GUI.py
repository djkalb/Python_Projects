


from cgitb import text
from tkinter import *
from tkinter import messagebox     
import tkinter

import Web_Page_Maker_Func    


class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #master frame configuration
        self.master = master
        self.master.minsize(500, 300) 
        self.master.maxsize(500,300)
        
        self.master.title("Web Page Generator")
        self.master.configure(bg= "#f0f0f0")
        #detects click in NE corner for red x
        self.master.protocol("WM_DELETE_WINDOW", lambda: Web_Page_Maker_Func.askQuit(self))
        
        self.lblField = Label(self.master, text="Enter Paragraph here: ")
        self.lblField.grid(row=0, column=0)
        #input for page header sadly cannot enlarge an entry form
        self.entryField = Entry(self.master, text = "", width=50)
        self.entryField.grid(row=1, column=0, columnspan=3, rowspan=3)

        #calls the function to make page
        self.btnSubmit = Button(self.master, text = "Create Page", command=lambda: Web_Page_Maker_Func.create(self))
        self.btnSubmit.grid(row = 5, column=0)

        


if __name__ == "__main__":
    root = tkinter.Tk()  
    App = ParentWindow(root)
    root.mainloop()       


    


    