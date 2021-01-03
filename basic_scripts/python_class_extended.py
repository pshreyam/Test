f_name = input("Enter your name: ")
l_name = input("Enter your last name: ")
e_age = input("Enter your age: ")

class Employee():
    def __init__(self, fname, lname, age):
        self.fname = fname.title()
        self.lname = lname.title()
        self.age = age
        self.email = fname + "." + lname + "@company.edu.np"

for i in range(1, 5):
    emp = Employee(f_name,l_name,e_age)
    print(emp.fname)
    print(emp.lname)
    print(emp.age)
    print(emp.email)

