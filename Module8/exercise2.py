names = set()  #note: set a empty set by using built-in function sec()
#if write like names = {}, system regards it a empty dictionary
name = input("Enter a name: ")
while name != '':
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
    name = input("Enter a name: ")

for name in names:
    print(name)