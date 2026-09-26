from functions.level_challenge import level_challenge
from functions.interest_challenge import interest_challenge

def start_game(player):
    print("Firstly please read the challenge_introduction carefully")
    with open("challenge_introduction.txt", "r") as file:
        data = file.read()
        print(data)
    print("Here are two challenges for you!")
    print("1. level_challenge\n2. interest_interest")
    challenge = input("Now please choose the challenge you want to take: ")
    if challenge == "1":
        level_challenge(player)
    elif challenge == "2":
        interest_challenge(player)
    else:
        print("Invalid input")
        challenge = input("Now please choose the challenge you want to take: ")
    


    