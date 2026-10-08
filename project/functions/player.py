#Here create a player class, initialized information regarding name, age, Finnish level, and personal interests.
#Also three functions in the class. edit_information function allows player to change his information if he needs.
#build_finnish_library function allows player to create his own finnish vocabulary lists.
#practice_library function allows player to practice own finnish library.

class Player:
    def __init__(self, name, age, finnish_level, interest):
        self.name = name
        self.age = age
        self.finnish_level = finnish_level
        self.custom_finnish_library = {}
        self.interest = interest
        
    def edit_information(self):
        while True:
            print("Please choose the information you want to edit: ")
            print("1. name\n2. age\n3. finnish_level\n4. interest\n5. changes finish")
            choice = input("Please choose(just number is ok): ")
            if choice == "1":
                self.name = input("Enter a new name here: ")
                print("The name has been changed successfully!")
            elif choice == "2":
                self.age = input("Enter you age here: ")
                print("The age has been changed successfully!")
            elif choice == "3":
                self.finnish_level = input("Enter your current finnish_level here(0, A1, A2, B1, B2): ")
                print("Your finnish_level information has been updated!")
            elif choice == "4":
                self.interest = input("Enter your current interest here(nature, culture, life, food, sports): ")
                print("Your interest information has been updated!")
            elif choice == "5":#Exit the loop once all modifications are complete.
                print("OK, now all changes have finished.")
                print(f"Your new player information:\n1. Name: {self.name}\n2. Age: {self.age}\n3. Finnish_level: {self.finnish_level}\n4. Interest: {self.interest}")
                break
            else:
                print("Invalid input, please enter again.")

    def build_finnish_library(self):
        print("You can customize your own Finnish language library here.")
        finnish_word = input("Please enter the word you would like to add(Press Enter to finish adding.): ")
        while finnish_word != "":
            word_meaning = input("Please also enter the meaning of the word here: ")
            confirm = input(f"Are you sure to add {finnish_word}: {word_meaning} to the library?(y/n)")
            if confirm == "y":
                self.custom_finnish_library[finnish_word] = word_meaning
                print(f"The word {finnish_word} has been successfully added.")
            else:
                print(f"Word {finnish_word} is not added, please add again.")
            finnish_word = input("Please enter the word you would like to add(Press Enter to finish adding.): ")
        else:
            print("You have successfully created your own Finnish language library.")      
            print(self.custom_finnish_library) 

    def practice_library(self):
        print(f"Welcome {self.name}. You can practice your own library here!")
        if not self.custom_finnish_library:
            print("The Finnish library is empty now!")
            print("Please create your own Finnish library first.")
            return
        for word in self.custom_finnish_library:#Iterate over the keys in the dictionary
            print(word)
            meaning = input(f"Please enter the meaning of finnish word {word}: ")
            if self.custom_finnish_library[word] == meaning:
                print("Right!")
            else:
                print("Sorry, the meaning is wrong.")
                print(f"The correct meaning of {word} is {self.custom_finnish_library[word]}")
            continue_exit = input("Do you want to continue practice?(y/n)")
            if continue_exit == "n":
                print("Now practice has been ended.")
                return
        print("Congratulations, you have practiced all your custom words.")