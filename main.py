#Rock Paper Scissor Game using Python

import random
user_input = input("Enter a Choice : [R] - Rock, [P] - Paper, [S] - Scissor : ")
possibleAction = ["rock", "paper", "scissor"]
computerAction = random.choice(possibleAction)

if user_input == "r" or "R":
    if computerAction == "rock" :
        print("It's a Tie!")
    elif computerAction == "paper" :
        print("Ah! You just Lost to the Computer")
    else :
        print("Congo! You won against the Computer")
elif user_input == "p" or "P":
    if computerAction == "rock" :
        print("Congo! You won against the Computer")
    elif computerAction == "paper" :
        print("It's a Tie!")
    else :
        print("Ah! You just Lost to the Computer")
elif user_input == "s" or "S":
    if computerAction == "rock" :
        print("Ah! You just Lost to the Computer")
    elif computerAction == "paper" :
        print("Congo! You won against the Computer")
    else :
        print("It's a Tie!")
else:
    print("Invalid Choice!")