def offer_choice():
    print("\nAirport Data Management")
    print("1. Enter a new airport\n2. Fetch airport information\n3. Quit")
    number = input("Please choose an option (1-3): ")
    return number
choice = offer_choice()
airports = {}
while choice != '3':
    if choice == "1":
        code = input("Enter the ICAO code: ")
        name = input("Enter the airport name:")
        airports[code] = name
        print(f" Airport {name} with ICAO code {code} has been added.")
        choice = offer_choice()
    elif choice == '2':
        code = input("Enter the ICAO code: ")
        if code in airports:
            print(f"The airport with ICAO code {code} is {name}.")
        else:
            print(f"No airport found with ICAO code {code}.")
        choice = offer_choice()
if choice == '3':
    print("Thank you for using the Airport Data Management system. Goodbye!")
