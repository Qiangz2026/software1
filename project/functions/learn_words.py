#This function shows players can study the vocabulary list associated with their chosen challenge.
#The function receives player information and the words library and study one by one

def learn_words(player, challenge_words):
    for word, meaning in challenge_words.items():
        print(word)
        print(f"The meaning of word {word} is {meaning}.")
        choice = input("Would you like to continue to learn?(y/n)")
        if choice.lower() == "n":
            print("OK, now learning process has been ended.")
            return
    print(f"Good, {player.name}. You have already study all words of the library.")