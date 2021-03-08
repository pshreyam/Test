from python_stack import Stack

user = input("Enter a string:")
user_length = len(user)

s1 = Stack(user_length)
s2 = Stack(user_length)

for c in user:
    s1.push(c)

s1.view_stack()

reverse = ''

for c in user:
    reverse = reverse + s1.pop()
    
print(reverse)