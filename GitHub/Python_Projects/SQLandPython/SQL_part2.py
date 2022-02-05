import sqlite3

firstName = input("enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("enter your age: "))


with sqlite3.connect('test_database.db') as conn:
    c = conn.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName + "', '" + lastName + "', " + str(age) + ")"
    print(line)
    c.execute(line)
c.close()