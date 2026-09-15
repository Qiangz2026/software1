with open("save.txt", "w") as file:
    file.write("Player reached level 2.\n")
    file.write("Player reached level 3.\n")

with open("save.txt", "r") as file:
    data = file.read()#reads the entire contents of the file and stores it in the variable data
    print(data)
