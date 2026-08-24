# rounds = int(input("Enter the amount of greetingss time: ")) #Remember to convert the variable type.
# finish_rounds = 0
# while finish_rounds < rounds:
#     print("Good morning.")
#     finish_rounds = finish_rounds + 1

# command = input("Enter command: ")
# while command != "stop":
#     print(command)
#     command = input("Enter command: ")
# print("stop")

first = 1
while first <= 5:
    second = 1
    while second <= 5:
        product = first * second
        #print(str(first) + " times " + str(second) + " is " + str(product))
        print(f"{first} times {second} is {product}")
        second = second + 1
    first = first + 1

# import math

# print(f"{'Pi':1s}:{math.pi:.5f}")
# print(f"{'e':1s}:{math.e:.5f}")