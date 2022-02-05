from tkinter import *
import tkinter as tk

from numpy import var
import GUI_Func_5

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)
        self.master = master
        self.master.resizable(width = False, height=False)
        self.master.geometry('{}x{}'.format(510, 200))
        self.master.title('Check Files')

        
        self.btnSubmit = Button(self.master, text="Browse...", command=lambda: GUI_Func_5.btnBrowse(self), width=13)
        self.btnSubmit.grid(row=0, column=0, pady = (45, 0), padx = (20, 15), sticky=NE)

        self.btnCancel = Button(self.master, text="Browse...", command=lambda: GUI_Func_5.btnBrowse(self), width=13)
        self.btnCancel.grid(row=1, column=0, pady = (10, 0), padx = (20, 15), sticky=NE)

        self.var = StringVar()

        self.txtFName0 = Label(self.master, font=("Helvetica", 16), fg="black", bg="white", textvariable = self.var, width= 28)
        self.txtFName0.grid(row=0, column=2, columnspan = 3, pady = (45, 0), padx = (15, 0))

        self.txtFName1 = Label(self.master,  font=("Helvetica", 16), fg="black", bg="white", textvariable = self.var, width= 28)
        self.txtFName1.grid(row=1, column=2, columnspan = 3, pady = (10, 0), padx = (15, 0))

        self.btnSubmit = Button(self.master, text="  Check for files... ",  height=3)
        self.btnSubmit.grid(row=2, column=0,  pady = (10, 10), padx = (5, 0))

        self.btnCancel = Button(self.master, text="Close Program", command = lambda: GUI_Func_5.close(self),width=15, height=3)
        self.btnCancel.grid(row=2, column= 4, pady = (10, 10), padx=(0, 0), sticky=E)

        







if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

