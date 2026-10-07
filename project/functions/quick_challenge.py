from finnish_word import random_words
from .run_challenge import run_challenge

def quick_challenge(player):
    print(f"Hi, player.name. Welcome to the challenge!")
    challenge_words = random_words
    run_challenge(player, challenge_words)