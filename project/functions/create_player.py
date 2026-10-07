from .player import Player

def create_player():
    player_name  = input("Hi, enter your name here: ")
    player_age = int(input("Please also enter your age: "))
    finnish_level = input("Please also enter your Finnish level here(0, A1, A2, B1, B2): ")
    interest = input("Please enter here your interest about Finnish words(nature, culture, life, food, sports): ")
    player = Player(player_name, player_age, finnish_level, interest)
    print("Thank you for the information and the player is created now!")
    return player