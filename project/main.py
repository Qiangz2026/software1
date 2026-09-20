from functions import menu, game_introduction, Create_player, finnish_library, practice_library, start_game, exit_game 

game_name = "Finnish learning challenge!"
print(f"Welcome to {game_name}")
player_name  = input("Hi, enter your name here: ")
player_age = int(input("Please also enter your age: "))
if player_age < 12:
    print("Sorry, you are a minor. Please close the game.")
else:
    print(f"Hi, {player_name}. Welcome to the game.")
    print("Here is the menu for you!")
    choice = menu()
    current_words = []#Initial list of the custom finnish library
    game_process = True
    while game_process:
        if choice == "1":
            game_introduction()
            choice = menu()
        elif choice == "3":
            current_words = finnish_library()
            choice = menu()
        elif choice == "4":
            start_game()
            game_process = False
        elif choice == "5":
            if not current_words:
                print("The Finnish library is empty now!")
                print("Please create your own Finnish library first.")
            else:
                practice_library(current_words)
            choice = menu()
        elif choice == "6":
            exit_game()
            game_process = False
        else:
            print("Your input is wrong, please try again.")
            choice = menu()