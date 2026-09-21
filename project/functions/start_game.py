#Pass a `player` parameter to the function—containing the player's name, age, and Finnish level—and match the vocabulary library based on that level.
def start_game(player):
    print("Firstly please read the challenge_introduction carefully")
    with open("challenge_introduction.txt", "r") as file:
        data = file.read()
        print(data)
    print("1. Nature\n2. Life\n3.Culture\n4. Mix")
    topic = input("Now please select the topic you would like to challenge.")
    if topic == "1":
        with open("Nature_A1.1.txt", "r") as file:
            for line in file:
                print(line.strip())


    