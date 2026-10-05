from finnish_word import level_0_words, level_a1_words, level_a2_words
from finnish_word import level_b1_words, level_b2_words
import random

def level_challenge(player):
    print("Welcome to the level challenge!")
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
    choice = input("Please choose:\n1. Learn words firstly\n2. Start challenge right now.")
    if choice == "1":
        for word, meaning in challenge_words.items():
            print(word)
            print(f"The meaning of word {word} is {meaning}.")
    elif choice == "2":
        print(f"Your current level is {player.finnish_level}, now generating the corresponding challenge for you.")
        for word, meaning in random.sample(list(challenge_words.items()), k=5):
            print(f"What is the meaning of word {word}?")
            answer = input("Please enter your answer here: ")
            if answer == meaning:
                print("Correct!")
            else:
                print(f"Your answer is wrong and the correct meaning is {meaning}.")
    else:
        print("Invalid input")