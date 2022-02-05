import shutil
import os
import time
import tkinter
import tkinter.filedialog
import file_transfer_GUI
from tkinter import messagebox


def fileTransfer(self):
    if self.source.get() == '' or self.destination.get() == '' or self.source.get() == self.destination.get():
        messagebox.showerror("field missing", "ensure source and destination are chosen")
    
    
    files= os.listdir((self.source.get()))

    for i in files:
       
        # grabs seconds passed since epoch
        epoch_time = int(time.time())
        #returns seconds passed since epoch up to last mod
        modded = os.path.getmtime((self.source.get())+ '/' + i)
        #moves files if the have been modded in the last day 86400 is just num of secs in day
        if modded > (epoch_time - 86400):
            
            shutil.move((self.source.get()) + '/' + i, (self.destination.get()))
        messagebox.showinfo("transfer completed", "the files have been moved")
                




def btnBrowse(self, btn):
    path = tkinter.filedialog.askdirectory()
    if btn == 0:
        
        self.source.set(path)
    else:
        self.destination.set(path)
        
    
    
    
    
def close(self):
    self.master.destroy()
    
        
