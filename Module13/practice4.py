#error handling
# try:
#     with open("save.txt", "r") as file:
#         data = file.read()
# except FileNotFoundError:
#     print("File not found.")
# except IOError:
#     print("Error occurred while handling the file.")

try:
    player_age = int(input("Enter player's age: "))
except ValueError:
    print("Error: entered value is not an integer.")
print("Program execution continues.")