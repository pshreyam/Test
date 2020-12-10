number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
try:
    answer=(number1/number2)
except ZeroDivisionError:   #Exception
    print("Not divisible by zero.")
else:
    print("Answer: ",answer)
