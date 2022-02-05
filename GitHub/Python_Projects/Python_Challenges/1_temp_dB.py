import sqlite3


with sqlite3.connect(':memory:') as conn:
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        IQ INTEGER
    )""")
    c.execute(""" INSERT INTO Roster VALUES 
    ('Jean-Baptiste Zorg', 'Human', 122);""")
    c.execute(""" INSERT INTO Roster VALUES 
    ('Korben Dallas', 'Meat Popsicle', 100);""")
    c.execute(""" INSERT INTO Roster VALUES 
    ("*Ak'not*", 'Mangalore', -5);""")
    
    c.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")
    c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
c.close()