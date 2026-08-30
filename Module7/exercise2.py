import random

def roll_dice(sides):
    number = random.randint(1,sides)
    return number

max_number = int(input("Enter the max number you want to get: "))
number = roll_dice(max_number)
while number != max_number:
    print(number)
    number = roll_dice(max_number)
else:
    print(number)

