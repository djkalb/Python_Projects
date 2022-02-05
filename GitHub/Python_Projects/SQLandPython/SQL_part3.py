import sqlite3


firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
data = (firstName, lastName, age)

with sqlite3.connect('test_database.db') as conn:
    c = conn.cursor()
    c.execute("INSERT INTO People VALUES (?,?,?)", data) 
    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?", (45, 'Luigi', 'Vercotti'))

c.close()
