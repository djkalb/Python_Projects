import os

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3



import student_gui
import student_main



#get rid of add and update  remove all references of phonebook / revised phrases
#add course behaviour and add submit func

def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width/2) - (w/2))
    y = int((screen_height / 2) - (h/2))
    centerGeo = self.master.geometry('{}x{} + {} + {}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)



def create_db(self):
    conn = sqlite3.connect('db_users.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_students(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            col_fname TEXT,\
            col_lname TEXT,\
            col_fullname TEXT,\
            col_phone TEXT,\
            col_email TEXT,\
            col_course\
            );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    data = ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@gmail.com', 'c#')
    conn = sqlite3.connect('db_users.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            #text went off screen need rest of this line
            cur.execute("""INSERT INTO tbl_students (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?,?,?,?,?,?)""", (data))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT (*) FROM tbl_students""")
    count = cur.fetchone()[0]
    return cur, count
def onSelect (self, event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_users.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname, col_lname, col_phone, col_email, col_course FROM tbl_students WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        for data in varBody:
            self.txt_fname.delete(0, END)
            self.txt_fname.insert(0, data[0])
            self.txt_lname.delete(0, END)
            self.txt_lname.insert(0, data[1])
            self.txt_phone.delete(0, END)
            self.txt_phone.insert(0, data[2])
            self.txt_email.delete(0, END)
            self.txt_email.insert(0, data[3])
            self.txt_course.delete(0, END)
            self.txt_course.insert(0, data[4])
            

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()

    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()

    var_fullname = ("{} {}".format(var_fname, var_lname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()

    if not "@" or not "." in var_email:
        print("incorrect email format")
    if(len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0):
        conn = sqlite3.connect('db_users.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_students WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: 
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_students (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?, ?,?,?,?, ?)""", (var_fname, var_lname, var_fullname, var_phone, var_email, var_course))
                self.lstList1.insert(END, var_fullname)
                onClear(self)
            else:
                messagebox.showerror("Name Error", "'{}' already exists in the database! pick a different name".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error", "Please recheck the data")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('db_users.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT (*) FROM tbl_students")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_users.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_students WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self)
                conn.commit()
        else: 
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and connot be deleted".format(var_select))
    conn.close()

def onDeleted(self):
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)

    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    self.txt_course.delete(0, END)

#combines adding to list and updating item into one general submit function
def onSubmit(self):
    addToList(self)
    onRefresh(self)
    
    
    
    

def onRefresh(self):
    self.lstList1.delete(0, END)
    conn = sqlite3.connect('db_users.db')
    with conn:
        cursor= conn.cursor()
        cursor.execute("""SELECT COUNT (*) FROM tbl_students""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_students""")
            varList = cursor.fetchall()[i]
            for item in varList: 
                self.lstList1.insert(0, str(item))
                i = i + 1
    conn.close()


def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0]
        var_value = self.lstList1.get(var_select)
    except:
        messagebox.showinfo("Missing selection, no name was selected. cancelling request")
        return
    
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0 and len(var_email) > 0):
        conn = sqlite3.connect('db_users.db')
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT COUNT (col_phone) FROM tbl_students WHERE col_phone = ' {} '""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT (col_email) FROM tbl_students WHERE col_email = ' {} '""".format(var_email))
            count2 = cur.fetchone()[0]
            if count == 0 or count2 == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) and ({}) will be implemented for ({})".format(var_phone, var_email, var_value))
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_students SET col_phone = '{}', col_email = '{}' WHERE col_fullname = '{}'""".format(var_phone, var_email, var_value))
                        onClear(self)
                    conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to {}".format(var_value))
    else:
        messagebox.showinfo("No changes detected", "Both fields were already in the database. Update cancelled")
    onClear(self)
    conn.close()
    











if __name__ == "__main__":
    pass