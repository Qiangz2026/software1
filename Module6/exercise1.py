import random
number = int(input("How many dice to roll: "))
sum = 0
for n in range(1,number+1):  
    dice_number = random.randint(1,6) #Simulated dice generate possible values
    sum += dice_number # The sum of the values ​​of each die is added together in a loop.
print(f"Sum of the dice: {sum}")