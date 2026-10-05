from finnish_word import nature_words, life_words, culture_words
from finnish_word import food_words, sports_words
import random

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