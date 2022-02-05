from tkinter import *
import tkinter as tk
import GUI_4
import tkinter.filedialog


def btnBrowse(self):
    path = tkinter.filedialog.askdirectory()
    self.var.set(path)
    
    
    return 
def close(self):
    self.master.destroy()
        



if __name__ == "__main__":
    pass