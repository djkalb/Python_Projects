import webbrowser
from tkinter import *
from tkinter import messagebox     

import os









def askQuit(self):
    
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def create(self):
    #opens the html file/ creates it if it doesnt exist
    #will overwrite file everytime so the inputs cant mess each other up
    with open("sale.html", 'w') as f:
        f.write("""
        <html>

            <body>

                <h1>

                    {}

                </h1>

                
                

            </body>

        </html>""".format(self.entryField.get()))
    
    f.close()
    #opens the html in new window
    webbrowser.open_new("sale.html")