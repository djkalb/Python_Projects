


class User:
    

    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account

    def login(self):
        entry_email = input("enter your email: ")
        entry_password = input("enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print('welcome back {}!we\'ve missed you'.format(self.name))
        else:
            print("please input a valid login")
new_user = User("james", "j@g.com", 'password', 1234)

class Employee(User):
    def __init__(self, pay, title):
        self.pay = pay
        self.title = title
class Admin(User):
    def __init__(self, privelidges, auth):
        self.privelidges = privelidges
        self.auth = auth
new_admin = Admin("all", "none")
new_Employee = Employee(6.00, "help")

print(new_Employee.title)

