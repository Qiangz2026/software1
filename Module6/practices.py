
# names = ["James","Julius","Jenny","Jane"] # Given an initial list
# print(names[1])  #just print name
# print(names[-2]) #just print name
# print(names[0:2]) #Includes left-hand index but excludes right-hand index, output is shown as a list format
# print(names)
# print(len(names)) #len()function is to show the length of the list
# names.append("Timo")
# print(names)
# names.remove("Jenny")
# print(names)
# names.insert(1,"Ulla") #Insert a name at a specified position
# print(names)
# print(names[4])  out of range

# names = []
# name = input("Enter your first name or quit by pressing Enter: ")
# while name != "":
#     names.append(name) #add input to list names
#     name = input("Enter your first name or quit by pressing Enter: ")
# print(names)
# names.pop(-1) #Delete the last element of the list. names.remove(-1) is not correct
# print(names)

# names = []
# name = input("Enter a name or quit by typing Enter: ")
# while name != "":
#     names.append(name) #Add the inputs to the list one by one.
#     name = input("Enter a name or quit by typing Enter: ")
# print(names)
# for i in names: #Accessing the list items one by one
#     print(f"hello,{i}")

random = range(3,31,3)
for n in random:
    print(n)