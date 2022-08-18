"""Write a Python program to check whether a file exists."""

#Solution:

import os

path = input("Enter file path:")
if(os.path.isfile(path)):
    print("File exists")
else:
    print("Not exists")