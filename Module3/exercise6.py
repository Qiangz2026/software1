import random
digit1_1 = random.randint(0, 9)           # About line2,3,4, can use loop function later
digit1_2 = random.randint(0, 9)
digit1_3 = random.randint(0, 9)
digit1 = str(digit1_1) + str(digit1_2) + str(digit1_3)
digit2_1 = random.randint(1, 6)
digit2_2 = random.randint(1, 6)
digit2_3 = random.randint(1, 6)
digit2_4 = random.randint(1, 6)
digit2 = str(digit2_1) + str(digit2_2) + str(digit2_3) + str(digit2_4)
print("3-digit code: " + digit1)
print("4-digit code: " + digit2)