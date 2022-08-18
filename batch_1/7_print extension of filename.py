"""Write a Python program to accept a filename from the user and print the extension of that.

Sample filename : abc.java

Output : java"""

filename = input("Enter your file name :").split(".")
print(filename)
print("Extension file is :", filename[-1])
