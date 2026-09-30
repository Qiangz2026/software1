class Player:
    def __init__(self, name, age, finnish_level, interest):
        self.name = name
        self.age = age
        self.finnish_level = finnish_level
        self.custom_finnish_library = {}
        self.interest = interest
        
    def show_information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Finnish level: {self.finnish_level}")
        print(f"Interest: {self.interest}")

    def build_finnish_library(self):
        print("You can customize your own Finnish language library here.")
        finnish_word = input("Please enter the word you would like to add(Press Enter to finish adding.): ")
        while finnish_word != "":
            word_meaning = input("Please also enter the meaning of the word here: ")
            self.custom_finnish_library[finnish_word] = word_meaning
            print(f"The word {finnish_word} has been successfully added.")
            finnish_word = input("Please enter the word you would like to add(Press Enter to finish adding.): ")
            # 6word_meaning = input("Please also enter the meaning of the word here: ")
        else:
            print("You have successfully created your own Finnish language library.")      
            print(self.custom_finnish_library) 

    def practice_library(self):
        if not self.custom_finnish_library:
            print("The Finnish library is empty now!")
            print("Please create your own Finnish library first.")
        for word in self.custom_finnish_library:#Iterate over the keys in the dictionary
            print(word)
            meaning = input(f"Please enter the meaning of finnish word {word}: ")
            if self.custom_finnish_library[word] == meaning:
                print("Right!")
                answer = input("Do you want to continue practicing?(y/n):")
                if answer == "y":
                    continue
                elif answer == "n":
                    break
            else:
                print("Sorry, the meaning is wrong.")
                print (f"Would you like to check the correct meaning of {word}? or you want try again")
                choice = input("1. check the meaning\n2. try again")
                if choice == "1":
                    print(f"The correct meaning of {word} is {self.custom_finnish_library[word]}")
                elif choice == "2":
                    meaning = input(f"Please enter the meaning of finnish word {word}: ")
