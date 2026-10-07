from functions.menu import menu
from functions.load_player import load_player
from functions.game_introduction import game_introduction
from functions.player import Player
from functions.start_game import start_game
from functions.save_exit_game import save_exit
from functions.create_player import create_player

game_name = "Finnish learning and challenge game!"
print(f"Welcome to {game_name}")
player = load_player()#give the return of the function load_player to player
if player == None:
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
        game_process = False
    elif choice == "5":
        player.practice_library()
        choice = menu()
    elif choice == "6":
        save_exit(player)
        game_process = False
    else:
        print("Your input is wrong, please try again.")
        choice = menu()