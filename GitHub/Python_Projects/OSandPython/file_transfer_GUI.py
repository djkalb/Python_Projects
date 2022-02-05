"""

Users are now asking for a user interface to make using the script easier and more versatile.


Desired features of the UI:


Allow the user to browse and choose a specific folder that will contain the files to be checked daily.

Allow the user to browse and choose a specific folder that will receive the copied files.

Allow the user to manually initiate the 'file check' process that is performed by the script.

Add comments throughout your Python explaining your code.
"""

from tkinter import *
import tkinter as tk


import file_transfer_func

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)
        self.master = master
        self.master.resizable(width = False, height=False)
        self.master.geometry('{}x{}'.format(510, 200))
        self.master.title('Check Files')

        
        self.btnBrowse0 = Button(self.master, text="Browse...", command=lambda: file_transfer_func.btnBrowse(self, 0), width=13)
        self.btnBrowse0.grid(row=0, column=0, pady = (45, 0), padx = (20, 15), sticky=NE)

        self.btnBrowse1 = Button(self.master, text="Browse...", command=lambda: file_transfer_func.btnBrowse(self, 1), width=13)
        self.btnBrowse1.grid(row=1, column=0, pady = (10, 0), padx = (20, 15), sticky=NE)

        self.source = StringVar()
        self.destination = StringVar()


        self.txtFName0 = Label(self.master,  fg="black", bg="white", textvariable = self.source, width= 28)
        self.txtFName0.grid(row=0, column=2, columnspan = 3, pady = (45, 0), padx = (15, 0))

        self.txtFName1 = Label(self.master,  fg="black", bg="white", textvariable = self.destination, width= 28)
        self.txtFName1.grid(row=1, column=2, columnspan = 3, pady = (10, 0), padx = (15, 0))

        self.btnSubmit = Button(self.master, text="  Check for files... ",  height=3, command=lambda: file_transfer_func.fileTransfer(self))
        self.btnSubmit.grid(row=2, column=0,  pady = (10, 10), padx = (5, 0))

        self.btnCancel = Button(self.master, text="Close Program", command = lambda: file_transfer_func.close(self),width=15, height=3)
        self.btnCancel.grid(row=2, column= 4, pady = (10, 10), padx=(0, 0), sticky=E)

        







if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

