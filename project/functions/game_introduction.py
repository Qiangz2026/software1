#This function show the game introduction to the player by reading game_introduction txt

def game_introduction():
    print("Here is the game introduction for you.")
    with open("game_introduction.txt", "r") as file:
        data = file.read()
        print(data)