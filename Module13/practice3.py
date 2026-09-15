#deleting a file
import os

if os.path.exists("save.txt"):
    os.remove("save.txt")
else:
    print("file not found.")