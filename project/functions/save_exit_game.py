#This function saves the information of the player and exit the game successfully.

from functions import menu
import json

def save_exit(player):
    answer = input("Do you really want to exit the game? (y/n)")
    if answer == "y":
        player_data = {
            "name": player.name,
            "age": player.age,
            "finnish_level": player.finnish_level,
            "interest": player.interest,
            "custom_library": player.custom_finnish_library
        }
        with open("player_data.json", "w") as file:
            json.dump(player_data, file)
        print("Your data has been saved and now exit the game successfully!")
    elif answer == "n":
        print("Please continue your challenge.")
        choice = menu()