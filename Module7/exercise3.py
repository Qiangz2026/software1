def gallons_to_liters(quantity_gallons):
    liters = quantity_gallons*3.785
    return liters
    
quantity_gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
while quantity_gallons >= 0:
    liters = gallons_to_liters(quantity_gallons)
    print(f"{quantity_gallons} American gallons is {liters:.2f} liters.")
    quantity_gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
else:
    print("Program finished.")