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

def greet(greeting, times):
    for i in range(times):
        print(greeting + " round " + str(i+1))
    return
greet("hello",3)
greet("hi", 3)