length = float(input("Enter the length of the zander in centimeters: "))
if length < 42:
    missing_cm = 42 - length
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print("The fish was " + "{:.1f}".format(missing_cm) + " centimeters below the size limit.")
else:
    print("The zander meets the size limit.")