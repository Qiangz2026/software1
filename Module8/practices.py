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

# import random
# def cast():
#     # first = random.randint(1,6)
#     # second = random.randint(1,6)
#     (first, second) = (random.randint(1,6), random.randint(1,6))
#     #return first, second
#     return (first, second)
# #(die1,die2) = cast()
# die1, die2 = cast()
# print(f"The dice show {die1} and {die2}.")

# numbers = {"Viivi":"050-1234567",
#            "Ahmed":"040-1112223",
#            "Pekka":"050-7654321"}
# numbers["Olga"] = "050-1011012"
# numbers["Mary"] = "0401-2132139"
# print(numbers)
# name = input("Enter name: ")
# if name in numbers:
#     print(f"The phone number of {name} is {numbers[name]}.")

# Create a list named 'cars'
cars = [
    # First car (dictionary)
    {
        "make": "Toyota",
        "model": "Corolla",
        "year": 2018
    },
    # Second car (dictionary)
    {
        "make": "Ford",
        "model": "Focus",
        "year": 2020
    },
    # Third car (dictionary)
    {
        "make": "VW",
        "model": "ID.3",
        "year": 2023
    }
]
print("Information about the second car: ")
print(cars[1])
print(cars[1]["year"])
print(f"The year of the second car is {cars[1]['year']}")
print("Here are all cars information: ")
for car in cars:
    print(f"Make: {car['make']}, Model: {car['model']}, Year: {car['year']}.")