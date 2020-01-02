import random
def play(user):
    computer=['rock','paper','scissors']
    choice=random.choice(computer)   
    if(user=="rock"):
        if (choice=="scissors"):
            return "User won.",choice
        elif(choice=="paper"):
            return "User lost.",choice
        else:
            return "Tie.",choice
    elif(user=="paper"):
        if (choice=="scissors"):
            return "User lost.",choice
        elif(choice=="rock"):
            return "User won.",choice
        else:
            return "Tie.",choice
    elif(user=="scissors"):
        if (choice=="rock"):
            return "User lost.",choice
        elif(choice=="paper"):
            return "User won.",choice
        else:
            return "Tie.",choice
    




