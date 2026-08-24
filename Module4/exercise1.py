length = float(input("Enter the length of the zander in centimeters: "))
if length < 42:
    missing_cm = 42 - length
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    #print("The fish was " + "{:.1f}".format(missing_cm) + " centimeters below the size limit.")
    print(f"The fish was missing_cm:{missing_cm:.1f} cnetimeters below the size limit.") #Recommended formatted output method
else:
    print("The zander meets the size limit.")