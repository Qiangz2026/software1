import os
import json
from functions.player import Player

def load_player():
    if os.path.exists("player_data.json"):
        with open("player_data.json", "r") as file:
            player_data = json.load(file)
        player = Player(player_data["name"], player_data["age"], player_data["finnish_level"], player_data["interest"])
        player.custom_finnish_library = player_data["custom_finnish_library"]
        print(f"Hi, {player.name}. Welcome to the game again.")
        print("Player information loaded successfully.")
        return player
    else:
        print("Player not found, please create firstly.")
        return None