largest = None
smallest = None
while True:
    numbers = input("Enter a number (or press Enter to quit): ")
    if numbers == "":
        break
    numbers = float(numbers)
    if largest is None or numbers > largest:
        largest = numbers
    if smallest is None or numbers < smallest:
        smallest = numbers
print("Smallest number: " + str(smallest))
print("Largest number: " + str(largest))