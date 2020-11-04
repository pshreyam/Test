import random

def play(user):
    computer = ['rock', 'paper', 'scissors']
    
    choice = random.choice(computer)
    
    if user == choice:
    	return "Tie.", choice
       
    if user == "rock":
        if choice == "scissors":
            return "User won.", choice
        else:
            return "User lost.", choice
        
    elif user == "paper":
        if choice == "scissors":
            return "User lost.", choice
        else:
            return "User won.", choice
     
    else:
        if choice == "rock":
            return "User lost.", choice
        else:
            return "User won.", choice
