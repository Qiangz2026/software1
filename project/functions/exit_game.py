def exit_game():
    answer = input("Do you really want to exit the game? (y/n)")
    if answer == "y":
        print("Your data has been saved and now exit the game successfully!")
    elif answer == "n":
        print("Please continue your challenge.")