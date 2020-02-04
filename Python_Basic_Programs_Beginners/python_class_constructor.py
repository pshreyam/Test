#implementing constructor in a python class
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'

    #defining a function with parameter self
    def fullname(self):
        print(self.first+" "+self.last)
        

        
#instance of a class
emp_1=Employee("Ram","Lakhan",2000)
emp_2=Employee("Gopi","Chand",5000)
print(emp_1.email)
emp_1.fullname()
#print(emp_2.email)
#emp_2.fullname()
#just for practice
print(emp_1.first+" and "+emp_2.first+" are very good friends with emails: "+emp_1.email+" and "+emp_2.email+" respectively!!!") 
        
