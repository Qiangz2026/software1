# 
# names = ["James","Julius","Jenny","Jane"] # Given an initial list
# print(names[1])  #just print name
# print(names[-2]) #just print name
# print(names[0:2]) #Includes left-hand index but excludes right-hand index, output is shown as a list format
# print(names)
# print(len(names)) #len()function is to show the length of the list
# # print(names[4])  out of range

names = []
name = input("Enter your first name or quit by pressing Enter: ")
while name != "":
    names.append(name) #add input to list names
    name = input("Enter your first name or quit by pressing Enter: ")
print(names)