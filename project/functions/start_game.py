#This function shows challenge_introduction to the player by reading the introduction txt.
#Also player can choose the challenge that he wants to take from three challenges.

from .level_challenge import level_challenge
from .interest_challenge import interest_challenge
from .quick_challenge import quick_challenge

def start_game(player):
    print("Firstly please read the challenge_introduction carefully!")
    with open("challenge_introduction.txt", "r") as file:
        data = file.read()
        print(data)
    print("Here are three simple challenges for you!")
    while True:
        print("1. level_challenge\n2. interest_challenge\n3. quick_challenge\n4. Back")
        choice = input("Now please choose the challenge you want to take or go back to the main menu: ")
        if choice == "1":
            level_challenge(player)
        elif choice == "2":
            interest_challenge(player)
        elif choice == "3":
            quick_challenge(player)
        elif choice == "4":
            break
        else:
            print("Invalid input, please enter your choice again.")
        