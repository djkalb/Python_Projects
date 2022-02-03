from ast import operator
import sqlite3



conn = sqlite3.connect('user_db.db')


    
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_text_files (\
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                    file_name TEXT)")
    conn.commit()
conn.close()



def txtGrabber(lst):
    return ( _ for _ in lst if _.endswith("txt"))

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
    'myMovie.mpg', 'world.txt', 'data.pdf', 'myPhoto.jpg')  





for item in fileList:
    if item.endswith('txt'):
        conn = sqlite3.connect('user_db.db')
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_text_files (file_name) VALUES (?)", (item,))
            print(item)
            
        conn.close()
        

     
    




