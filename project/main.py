from functions import menu, game_introduction, Player, start_game, exit_game 

game_name = "Finnish learning challenge!"
print(f"Welcome to {game_name}")
player_name  = input("Hi, enter your name here: ")
player_age = int(input("Please also enter your age: "))
if player_age < 12:
    print("Sorry, you are a minor. Please close the game.")
else:
    print(f"Hi, {player_name}. Welcome to the game.")
    finnish_level = input("Please also enter your Finnish level here(A1.1, A1.2, A1.3, B1, B2): ")
    interest = input("Please enter here your interest about Finnish words(Nature, Culture, Life):")
    player = Player(player_name, player_age, finnish_level, interest)#create player using class Create_player
    print("Thank you for the information and the player is created now!")
    print("Here is the menu for you!")
    choice = menu()
    game_process = True
    while game_process:
        if choice == "1":
            game_introduction()
            choice = menu()#Display the menu to the player again after they finish reading the game instructions.
        elif choice == "2":
            player.show_information()
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
            exit_game()
            game_process = False
        else:
            print("Your input is wrong, please try again.")
            choice = menu()