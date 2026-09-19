def practice_library(words):
    for word in words:
        answer = input("Do you want to continue practicing?(y/n):")
        if answer == "y":
            print(word)
        elif answer == "n":
            break
        