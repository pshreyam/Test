'''#using break
available=5
n=int(input("Enter the number of candies:"))
i=1
while (i<=n):
    if (i>available):
        r=n-available
        print("We've run out of stock.{",r," remaining}")
        break
    print("Lucky!!!You've got your candies!")
    i=i+1
print("Bye!") '''   

#using continue
n=int(input("Enter the number->"))
for i in range (1,n+1):
    if (i%3==0 or i%5==0):
        continue
    else:
        print(i)
        
     
