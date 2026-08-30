import random

def roll_dice():
    number = random.randint(1,6)
    return number

number = roll_dice()
while number != 6:
    print(number)
    number = roll_dice() #update value of value
else:
    print(number)