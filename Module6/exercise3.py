number = input("Enter an integer: ")
number = int(number)
if number <= 1:
    print(f"{number} is not a prime number.")
elif number == 2:
    print(f"{number} is a prime number.")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
        elif i == (number - 1):
            print(f"{number} is a prime number.")