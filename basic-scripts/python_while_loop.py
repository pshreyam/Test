#using while loop & implementing palindrome number tests
n=int(input("Enter a number:->"))
temp=n
add=0
while (temp>0):
    r=temp%10
    add=(add*10)+r
    temp=temp//10
print (add)
if (add==n):
    print ("It is a palindrome number.")
else:
    print("It is not a palindrome number.")
