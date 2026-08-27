import random
total_number = input("Please enter the number of random points: ") 
total_number = int(total_number)
i = 0
n = 0
while i < total_number:
    x = random.uniform(-1,1) #Simulated x-coordinate
    y = random.uniform(-1,1) #Simulated y-coordinate
    if (x**2 + y**2) < 1:
        n += 1
    i += 1
pi = 4*n/total_number
print(f"Approximation of pi: {pi}")
