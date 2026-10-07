##This function is the level_challenge of the game. 
#First according to the finnish_level information of the player, select the finnish words library, after that
#player can choose to learn the words or start challenge directly.

from finnish_word import level_0_words, level_a1_words, level_a2_words
from finnish_word import level_b1_words, level_b2_words
from .run_challenge import run_challenge
from .learn_words import learn_words

def level_challenge(player):
    print(f"Hi, {player.name}. Welcome to the level challenge!")
    player.finnish_level = player.finnish_level.upper()
    if player.finnish_level == "0":
        challenge_words = level_0_words
    elif player.finnish_level == "A1":
        challenge_words = level_a1_words
    elif player.finnish_level == "A2":
        challenge_words = level_a2_words
    elif player.finnish_level == "B1":
        challenge_words = level_b1_words
    elif player.finnish_level == "B2":
        challenge_words = level_b2_words
    print("Do you want to study all the words first before taking on the challenge, or start the challenge right away?")
    while True:
        choice = input("1. Learn words\n2. Start challenge right now.\nPlease choose:")
        if choice == "1":
            learn_words(player, challenge_words)
        elif choice == "2":
            print(f"Your current finnish level is {player.finnish_level}, now generating the corresponding challenge for you.")
            run_challenge(player, challenge_words)
            break
        else:
            print("Invalid input, please choose again.")