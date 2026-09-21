def practice_library(player):
    if not player.custom_finnish_library:
        print("The Finnish library is empty now!")
        print("Please create your own Finnish library first.")
    for word in player.custom_finnish_library:
        answer = input("Do you want to continue practicing?(y/n):")
        if answer == "y":
            print(word)
        elif answer == "n":
            break
        