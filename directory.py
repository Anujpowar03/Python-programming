import os

print("Current Directory : ",os.getcwd())

os.listdir()
print("List of files in current directory : ",os.listdir())

#os.mkdir("NewFolder")
#print("Directory 'NewFolder' created")

print("List of files in current directory : ",os.listdir())

#os.rename("NewFolder","RenamedFolder")
print("After renaming: ",os.listdir())

os.rmdir("RenamedFolder")
print("After removing: ",os.listdir())
