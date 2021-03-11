import random

wrongs = 5

class Difficulty:
    easy = "easy"
    medium = "medium"
    hard = "hard"

word_list = [
        {
            "word": "test",
            "description": "rhymes with rest",
            "difficulty": Difficulty.easy
        },
        {
            "word": "color",
            "description": "what is red?",
            "difficulty": Difficulty.easy
        },
        {
            "word": "corona",
            "description": "virus",
            "difficulty": Difficulty.medium
        },
        {
            "word": "python",
            "description": "programming language",
            "difficulty": Difficulty.hard
        }
]

print("Hangman:")

difficulty = input("Enter the level of difficulty [easy, medium, hard] : ")
if not difficulty in [Difficulty.easy, Difficulty.medium, Difficulty.hard]:
    print("Sorry! input not recognized. Setting difficulty to easy!")
    difficulty = Difficulty.easy
    
word_list = list(filter(lambda x: x["difficulty"] == difficulty.strip().lower(), word_list))

if word_list:
    obj = random.choice(word_list)
    word = obj["word"]
    guessed = ["_" for x in word]
    print(f"Description: {obj['description']}")
    
    won = False

    while wrongs > 0:
        print(f"You have {wrongs} wrong guesses left!")
        print("".join(guessed))

        guess = input("Enter your guess: ")

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            wrongs -= 1
            print(f"'{guess}' is not in the word!")
        
        if '_' not in guessed:
            won = True
        
        if won:
            break

    if won:
        print("You won!")
    else:
        print("You lost!")
else:
    print("Sorry we didn't find a word!")
