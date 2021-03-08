class admin():
    def __init__(self):
        pass
class user():
    def __init__(self,fname,lname,dob_year,dob_month,dob_date,username,password,gender):
         self.fname=fname.title()
         self.lname=lname.title()
         self.fullname=fname.title()+" "+lname.title()
         self.DOB=str(dob_year)+"/"+str(dob_month)+"/"+str(dob_date)
         self.gender=gender
         self.username=username
         self.password=password+"_hello_its_encrypted"
   
#main page:
print("* Welcome to our home page: *")
print("* Your Choices: *")
print("1. Sign up")
print("2. Sign in")
choice=int(input("Enter your choice:"))
print("----------------------------------------------------------------------------------------------")
while (choice!=1 or choice!=2):
            if (choice==1):
                print ("Sign up:")
                #signup 
                fname=str(input("Enter your first name:"))
                lname=str(input("Enter your last name:"))
                dob_year=int(input("Enter the year you were born:"))
                dob_month=int(input("Enter the month you were born:"))
                dob_date=int(input("Enter the date you were born:"))
                username=str(input("Enter a valid username for yourself:"))
                passwd=""
                repass="1"
                while (passwd!=repass):
                    passwd=str(input("Enter a strong password for yourself:"))
                    repass=str(input("Re-enter the password:"))
                    if (passwd!=repass):
                         print("Password do not match. Re-type password!")
                password=passwd
                gender=str(input("Enter your gender<M/F>:"))
                user_1=user(fname,lname,dob_year,dob_month,dob_date,username,password,gender)
                print("-------------------------------------------------------------------------------")
                print("Welcome to our Login page:")
                #signin
                user_name=str(input("Enter your username:"))
                pass_word=str(input("Enter your password:"))
                if (user_name==user_1.username):
                    if ((pass_word+"_hello_its_encrypted")==(user_1.password)):
                        print("Sign In Successful!!!" )
                        print("------------------------------------------------------------------------")
                        print("User status:")
                        print("Full name:",end="")
                        print(user_1.fullname)
                        print("Birthday:",end="")
                        print(user_1.DOB)
                        print("Username:",end="")
                        print(user_1.username)
                        print("Gender:",end="")
                        print(user_1.gender)
                        print("Password:",end="")
                        print(user_1.password)
                #signinend
                break
            elif (choice==2):
                lpassword="hello_hello_its_encrypted"
                fullname="Munna Bhai"
                DOB="2032/2/3"
                username="bmunna"
                gender="M"
                password=lpassword
                print("Log in:")
                #signin
                user_name=str(input("Enter your username:"))
                pass_word=str(input("Enter your password:"))
                if ((pass_word+"_hello_its_encrypted")==(lpassword)):
                    print("Sign In Successful!!!" )
                    print("")
                    print("User status:")
                    print("Full name:",end="")
                    print(fullname)
                    print("Birthday:",end="")
                    print(DOB)
                    print("Username:",end="")
                    print(username)
                    print("Gender:",end="")
                    print(gender)
                    print("Password:",end="")
                    print(password)
                    #signinend
                    break
            else:
                if (choice!=2 and choice!=2):
                    print("Not a valid option")





 
