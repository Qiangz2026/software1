import random
random_integer = random.randint(1,10)
while True:
    guess_number = input("Guess a number (1-10): ")
    guess_number = int(guess_number)
    if guess_number > random_integer:
        print("Too high")
    elif guess_number < random_integer:
        print("Too low")
    else:
        print("Correct")
