


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
    def __init__(self, pay, title, hours):
        self.pay = pay
        self.title = title
        self.hours = hours

    def overtimeCalc (self):
            if self.hours > 40:
                return ("Your new pay rate is {} keep working more hours".format(self.pay * 1.5))
    
    def login(self):
        entry_email = input("enter your email: ")
        entry_password = input("enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print('get to work {}. you are not getting paid to stand around'.format(self.name))
            return self.hours + 1
        else:
            print("please input a valid login")





class Admin(User):
    def __init__(self, privelidges, auth):
        self.privelidges = privelidges
        self.auth = auth
    def login(self):
        entry_auth = input("enter your authorization code: ")
        entry_password = input("enter your password: ")
        if (entry_auth == self.auth and entry_password == self.password):
            print('you are logged in. {} privelidges are granted'.format(self.privelidges))
        else:
            print("please input a valid login")

if __name__ == "__main__":
    new_admin = Admin("all", "none")
    new_Employee = Employee(6.00, "help", 41)
    new_Employee.email = 'asdf'
    new_Employee.password = 'password'
    new_admin.password = 'ishallpass'

    new_Employee.name = 'Ug'
    print(new_Employee.overtimeCalc())
    print(new_Employee.login())
    print(new_admin.login())