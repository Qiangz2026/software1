from functions import menu, game_introduction, Create_player, finnish_library, practice_library, start_game, exit_game 

game_name = "Finnish learning challenge!"
print(f"Welcome to {game_name}")
player_name  = input("Hi, enter your name here: ")
player_age = int(input("Please also enter your age: "))
finnish_level = input("Please also enter your Finnish level here(A1.1, A1.2, A1.3, B1, B2): ")
if player_age < 12:
    print("Sorry, you are a minor. Please close the game.")
else:
    print(f"Hi, {player_name}. Welcome to the game.")
    player = Create_player(player_name, player_age, finnish_level)#create player using class Create_player
    print("Here is the menu for you!")
    choice = menu()
    #current_words = []#Initial list of the custom finnish library
    game_process = True
    while game_process:
        if choice == "1":
            game_introduction()
            choice = menu()#Display the menu to the player again after they finish reading the game instructions.
        elif choice == "3":
            finnish_library(player)
            choice = menu()
        elif choice == "4":
            start_game(player)
            game_process = False
        elif choice == "5":
            practice_library(player)
            choice = menu()
        elif choice == "6":
            exit_game()
            game_process = False
        else:
            print("Your input is wrong, please try again.")
            choice = menu()