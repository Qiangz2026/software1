#Custom Finnish library

def finnish_library():
    print("You can customize your own Finnish language library here.")
    words = []
    word = input("Please enter the word you would like to add(Press Enter to finish adding.): ")
    while word != "":
        words.append(word)
        print("The word has been successfully added.")
        word = input("Please enter the word you would like to add(Press Enter to finish adding.): ")
    else:
        print("You have successfully created your own Finnish language library.")
    return words