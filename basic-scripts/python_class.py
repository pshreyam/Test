# implementation of classes and objects in python


class Employee:
    pass
    
    
emp_1 = Employee()
emp_2 = Employee()

emp_1.first = "Hira"
emp_1.last = "Lal"
emp_1.email = "Hira.Lal@company.com"
emp_1.pay = 60000

emp_2.first = "Gopi"
emp_2.last = "Chand"
emp_2.email = "Gopi.Chand@company.com"
emp_2.pay = 50000

    
print(emp_1.pay)
print(emp_2.pay)

print(emp_1.email)
