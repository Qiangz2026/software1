def menu():
    print("1. ohjeet: View game instructions")
    print("2. tavoite: Set target vocabulary")
    print("3. pelaa: Start challenge now")
    print("4. pisteet: View challenge record")
    print("5. lopeta: Exit game")
    choice = input ("Please choose: ")
    return choice

def instructions():
    print("Please read the instructions carefully.")

def target():
    print("Before starting the game, you can set a target number.")
    print("The minimum vocabulary target is 50. If nothing is entered or the entered number is less than 50, the default vocabulary target is 50.")
    target = int(input("Now enter your target number: "))
    if target <= 50:
        print("Your target has been set to the default value of 50.")
    else:
        print(f"Thank you, you have successfully set your goal {target}.")

def play():
    print("Start you challenge now!")

def history():
    print("You have challenged two times, and you have learned 500 words.")

def exit_game():
    answer = input("Do you really want to exit the game? (y/n)")
    if answer == "Y":
        print("Your data has been saved and now exit the game successfully!")
    elif answer == "N":
        print("Please continue your challenge.")

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
    game_process = True
    while game_process:
        if choice == "ohjeet":
            instructions()
            choice = menu()
        elif choice == "tavoite":
            target()
            choice = menu()
        elif choice == "pelaa":
            play()
            game_process = False
        elif choice == "pisteet":
            history()
            choice = menu()
        elif choice == "lopeta":
            exit_game()
            game_process = False
        else:
            print("Your input is wrong, please try again.")
            choice = menu()



