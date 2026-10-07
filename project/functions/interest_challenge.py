#This function is the interest_challenge of the game. 
#First according to the interest of the player, select the finnish words library, after that
#player can choose to learn the words or start challenge directly.

from finnish_word import nature_words, life_words, culture_words
from finnish_word import food_words, sports_words
from functions.run_challenge import run_challenge
from functions.learn_words import learn_words

def interest_challenge(player):
    print("Welcome to the level challenge!")
    if player.interest == "nature":
        challenge_words = nature_words
    elif player.interest == "life":
        challenge_words = life_words
    elif player.interest == "culture":
        challenge_words = culture_words
    elif player.interest == "food":
        challenge_words = food_words
    elif player.interest == "sports":
        challenge_words = sports_words
    print("Do you want to study all the words first before taking on the challenge, or start the challenge right away?")
    while True:
        choice = input("Please choose:\n1. Learn words\n2. Start challenge right now.")
        if choice == "1":
            learn_words(player, challenge_words)
        elif choice == "2":
            print(f"Your current interest is {player.interest}, now generating the corresponding challenge for you.")
            run_challenge(player, challenge_words)
            break
        else:
            print("Invalid input, please choose again.")