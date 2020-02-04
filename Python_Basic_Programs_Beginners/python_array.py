from array import *
student=array('i',[])
n=int(input("Input the no.of students->"))
for i in range(n):
    x=int(input("Enter the number:"))
    student.append(x)
for i in range(n):
    print (student[i])
