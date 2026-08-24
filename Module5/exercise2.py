length = float(input("Enter length in inches (negative value to quit): "))
while length >= 0:
    centimeters = length*2.54
    print(f"{length:.1f} inches is {centimeters:.2f} centimeters") #notice that is {length:.1f}, not {length:1f} to keep one decimal place
    length = float(input("Enter length in inches (negative value to quit): "))
print("Program ended.")