# money = float(input("Enter your money: "))
# if(money >= 5):
#     print("you can buy a latte.")
# else:
#     print("Your money is not enough.")


# cat = input("Enter the name of the cat: ")
# dog = input("Enter the name of the dog: ")
# if cat == dog:
#     print("The cat and the dog have the same name.")

# age = float(input("Enter your age: "))
# if 15 <= age < 18:
#     weight = float(input("Enter your weight: "))
# if age >= 18 or (age >= 15 and weight >= 55):
#     print("Medicine can be used.")
# else:
#     print("Medicine cannot be used.")

age = float(input("Enter your age: "))
if age >= 65:
    print("Your are retired.")
elif age > 18:
    print("You are working-aged.")
elif age >= 7:
    print("You are in school.")
else:
    print("You are a small child.")
