biological_gender = input("Enter biological gender (male/female): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))
biological_gender = biological_gender.lower()    #Convert all letters in the string biological_gender to lowercase.
if biological_gender == "female":
    if hemoglobin <= 117:
        print("Your hemoglobin is low.")
    elif 117 < hemoglobin < 155:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")
elif biological_gender == "male":
    if hemoglobin <= 134:
        print("Your hemoglobin is low.")
    elif 134 < hemoglobin <167:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")
else:
    print("Invalid gender.")