i = 0
while i < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "python" and password == "rules":
        print("Welcome")
        break         # here need to exit the loop after successfully logging in.
    else:
        i = i + 1
        if i < 5:
            print("Incorrect username or password. Please try again.")
        else:
            print("Access denied")