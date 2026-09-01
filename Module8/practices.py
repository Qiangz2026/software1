# #day_of_the_week = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
# day_of_the_week = "monday","tuesday","wednesday","thursday","friday","saturday","sunday"
# # Whether or not parentheses are used when creating tuples is optional, but it is recommended to use them.
# day_number = int(input("Enter the number of day(1-7): "))
# day = day_of_the_week[day_number-1]
# print(f"Day number {day_number} is: {day}.")

# fruits = "apple","pear","banana"
# #first, second, third = fruits    correct
# (first, second, third) = fruits
# #fruits = (first, second, third)   wrong
# print(f"Fruits are {first}, {second}, {third}.")

import random
def cast():
    # first = random.randint(1,6)
    # second = random.randint(1,6)
    (first, second) = (random.randint(1,6), random.randint(1,6))
    #return first, second
    return (first, second)
#(die1,die2) = cast()
die1, die2 = cast()
print(f"The dice show {die1} and {die2}.")