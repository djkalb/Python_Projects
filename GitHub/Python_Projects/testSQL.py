import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons (\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_fName TEXT,\
        col_lName TEXT,\
        col_Email TEXT\
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect("test.db")
with conn:
    cur = conn.cursor()
    
    cur.execute("INSERT INTO tbl_persons (col_fName, col_lName, col_email)  VALUES (?, ?, ?)",\
            ('Bob', 'Smith', 'bsmith@gmail.com'))
    cur.execute("INSERT INTO tbl_persons (col_fName, col_lName, col_email)  VALUES (?, ?, ?)",\
            ('Sarah', 'Jones', 'as12@gmail.com'))
    cur.execute("INSERT INTO tbl_persons (col_fName, col_lName, col_email)  VALUES (?, ?, ?)",\
            ('kevin', 'bacon', 'keev@gmail.com'))
    
    conn.commit()
conn.close()

conn = sqlite3.connect("test.db")
with conn:
    cur = conn.cursor()    
    cur.execute("SELECT col_fName, col_lName, col_Email FROM tbl_persons WHERE col_fName = 'Sarah'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {} \n Last Name: {} \n Email: {}".format(item[0], item[1], item[2])
    print(msg)
    conn.commit()
conn.close()


