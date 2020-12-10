import random

computer=['rock', 'paper', 'scissors']

def play(user, computer):  
    # a = random.randint(0,2)
    choice = random.choice(computer)
    
    print("Computer: ", choice)##we could also use #computer[a]    
    
    if user == "rock":
        if choice == "scissors":
            print("User won.")
        elif choice == "paper":
            print("User lost.")
        else:
            print("It is a tie.")
    
    elif user == "paper":
        if choice == "scissors":
            print("User lost.")
        elif choice == "rock":
            print("User won.")
        else:
            print("It is a tie.")
    
    elif user == "scissors":
        if choice == "rock":
            print("User lost.")
        elif choice == "paper":
            print("User won.")
        else:
            print("It is a tie.")

user = None

while user not in computer:    
    user = str(input("Enter:\n1.Rock\n2.Paper\n3.Scissors\n"))
    
    print("-" * 20)
    
    if user in computer:
        print("User: ", user)
        play(user, computer)
        break
    else:
        print("Not a valid one. Try again...\n")




