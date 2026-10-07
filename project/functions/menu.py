#This function mainly show the menu to player, get the choice of player and return the choice 

def menu():
    print("1. esittely: View game introduction")
    print("2. pelaaja: Edit player information")
    print("3. omavarasto: Custom Finnish Library")
    print("4. pelaa: Start challenge now")
    print("5. harjoittelu: Practice your Finnish library ")
    print("6. lopeta: Save and exit game")
    choice = input ("Please choose: ")
    return choice