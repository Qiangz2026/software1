import math

def calculate_unit_price(diameter, price):
    diameter_m = diameter/100      #Note the unit conversion. from cm to m.
    area = math.pi*(diameter_m/2)**2
    unit_price = price/area
    return unit_price
    
diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (euros): "))
diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (euros): "))
unit_price1 = calculate_unit_price(diameter1, price1)
unit_price2 = calculate_unit_price(diameter2, price2)
print(f"Unit price of the first pizza: {unit_price1:.2f} euros/m²")
print(f"Unit price of the second pizza: {unit_price2:.2f} euros/m²")
if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
elif unit_price1 > unit_price2:
    print("The second pizza provides better value for money..")