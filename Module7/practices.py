# def greet_user():
#     name = input("Enter your name here: ")
#     print(f"Hello, {name}")
#     return   # function end with a return statement. can also return a return value.
# greet_user()

# def greet(times):
#     for i in range(times):
#         print("Round" + str(i+1) + " of saying hello.")
#     return

# print("Let us start our day by saying hello.")
# print("How many times hello you want to say?")
# times = int(input("Enter a number here"))
# greet(times)

# def greet(greeting, times):
#     for i in range(times):
#         print(greeting + " round " + str(i+1))
#     return
# greet("hello",3)
# greet("hi", 3)

# def sum_of_squares(number1,number2):
#     result = number1**2 + number2**2
#     return result

# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))
# results = sum_of_squares(number1,number2)
# print(f"The sum of squares {number1:.3f} and {number2:.3f} is {results:.3f}.")

# List as a parameter
def show_items(items):
    print("You have the following items: ")
    for item in items:
        print("-" + item)
    # items.clear()
    return

list = ["apple","pear","banana"]
show_items(list)
list.append("peach")
show_items(list)