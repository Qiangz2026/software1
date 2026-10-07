from functions import menu
from functions import load_player
from functions import game_introduction
from functions import Player
from functions import start_game
from functions import save_exit
from functions import create_player
#The main function is responsible for loading existing players or creating new player, and displaying a menu that allows the player to access the program's various modules.

game_name = "Finnish learning and challenge game!"
print(f"Welcome to {game_name}")
player = load_player()#give the return of the function load_player to player
if player == None:
    player = create_player()
else:
    print("A saved player was found.")
    answer = input(f"Are you {player.name}?(y/n)")
    if answer.lower() == "y":
        print(f"Welcome back, {player.name}!")
    elif answer.lower() == "n":
        player = create_player()
print("Here is the menu for you!")
choice = menu()
game_process = True
while game_process:
    if choice == "1":
        game_introduction()
        choice = menu()#Display the menu to the player again after they finish reading the game instructions.
    elif choice == "2":
        player.edit_information()
        choice = menu()
    elif choice == "3":
        player.build_finnish_library()
        choice = menu()
    elif choice == "4":
        start_game(player)
        choice = menu()
    elif choice == "5":
        player.practice_library()
        choice = menu()
    elif choice == "6":
        save_exit(player)
        game_process = False
    else:
        print("Your input is wrong, please try again.")
        choice = menu()