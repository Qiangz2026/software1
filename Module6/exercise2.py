number = input("Enter a number: ")
numbers = []
while number != "":
    number = float(number)
    numbers.append(number)
    number = input("Enter a number: ")
numbers.sort(reverse=True)   #Sort the elements in the list from largest to smallest.
print("The greatest numbers in descending order: ")
if len(numbers) >= 5: #If the list contains five or more elements, Output the first five
    for n in numbers[0:5]:
        print(n)
else: #If there are fewer than five elements, output all of them.
    for n in numbers:
        print(n)