import sqlite3

conn = sqlite3.connect("test_database.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS People(FirstName TEXT, LastName TEXT, AGE INT)")
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")

c.close()

peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
with sqlite3.connect("test_database.db") as conn:
    c = conn.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, AGE INT);
                    INSERT INTO People VALUES('Ron', 'Obvious', 42);
                    """)
    c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues)
c.close()





