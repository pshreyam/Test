name=str(input("Enter your name please:"))
password=str(input("Enter your password please:"))
def passwordEncrypt(password):
    password1=password+"Hello"
    password=password1
    return password
print("Your name is:",name,"And the new password is:",passwordEncrypt(password))
