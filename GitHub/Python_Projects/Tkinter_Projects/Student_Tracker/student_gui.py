

from tkinter import *
import tkinter as tk
from tkinter import messagebox



import student_main
import student_func


def load_gui(self):
    self.varFName = StringVar()
    self.varLName = StringVar()



    self.lblFName = tk.Label(self.master, text ="First Name:")
    self.lblFName.grid(row=0, column=0, pady = (10, 0), padx = (27, 0), sticky=N+W)

    self.lblLName = tk.Label(self.master, text ="Last Name:")
    self.lblLName.grid(row=2, column=0, pady = (10, 0), padx = (27, 0), sticky=N+W)

    self.phone = tk.Label(self.master, text ="phone number:")
    self.phone.grid(row=4, column=0, pady = (10, 0), padx = (27, 0), sticky=N+W)

    self.email = tk.Label(self.master, text ="email address:")
    self.email.grid(row=6, column=0, pady = (10, 0), padx = (27, 0), sticky=N+W)

    self.course = tk.Label(self.master, text ="course:")
    self.course.grid(row=8, column=0, pady = (10, 0), padx = (27, 0), sticky=N+W)

    self.user = tk.Label(self.master, text ="user:")
    self.user.grid(row=0, column=2, pady = (10, 0), padx = (0, 0), sticky=N+W)
  
    self.txt_fname = tk.Entry(self.master, text="")
    self.txt_fname.grid(row=1, column=0, rowspan = 1, columnspan = 2, pady = (0, 0), padx = (30, 40), sticky=N+E+W)

    self.txt_lname = tk.Entry(self.master, text="")
    self.txt_lname.grid(row=3, column=0, rowspan = 1, columnspan = 2, pady = (0, 0), padx = (30, 40), sticky=N+E+W)

    self.txt_phone = tk.Entry(self.master, text="")
    self.txt_phone.grid(row=5, column=0, rowspan = 1, columnspan = 2, pady = (0, 0), padx = (30, 40), sticky=N+E+W)

    self.txt_email = tk.Entry(self.master, text="")
    self.txt_email.grid(row=7, column=0, rowspan = 1, columnspan = 2, pady = (0, 0), padx = (30, 40), sticky=N+E+W)

    self.txt_course = tk.Entry(self.master, text ="course:")
    self.txt_course.grid(row=8, column=0, rowspan = 1, columnspan = 2, pady = (30, 0), padx = (30, 40), sticky=N+E+W)

    #listbox and scrollbar
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event:student_func.onSelect(self, event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row = 1, column=5, rowspan = 7, columnspan= 1, padx=(0,0), pady= (0,0), sticky=N+E+S)
    self.lstList1.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0,0), pady=(0,0), sticky=(N+E+S+W))

    

    self.btnSubmit = Button(self.master, text="Submit", width=12, height=2, command=lambda:student_func.onSubmit(self))
    self.btnSubmit.grid(row=8, column=2, padx = (15, 0), pady = (45, 10), sticky=W)

    self.btnDelete = Button(self.master, text="Delete", width=12, height=2, command=lambda:student_func.onDelete(self))
    self.btnDelete.grid(row=8, column=4, columnspan= 1, padx = (15, 0), pady = (45, 10), sticky=E)




if __name__ == "__main__":
    pass

    
        

   














