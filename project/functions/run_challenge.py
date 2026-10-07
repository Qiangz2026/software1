import random
#This function receives player information and challenge_words as parameters.
#Calculate the score based on the player's answers to the five questions, and output whether the challenge was successful.

def run_challenge(player, challenge_words):
    point = 0
    for word, meaning in random.sample(list(challenge_words.items()), k=5):
        print(f"What is the meaning of word {word}?")
        answer = input("Please enter your answer here: ")
        if answer == meaning:
            print("Correct!")
            point += 1
        else:
            print(f"Your answer is wrong and the correct meaning is {meaning}.")
    print(f"Challenge is over and your score is: {point}")
    if point >= 4:
        print(f"Congratulations, {player.name}. You have successfully completed the challenge.")
    else:
        print("Unfortunately, this challenge is failed.")