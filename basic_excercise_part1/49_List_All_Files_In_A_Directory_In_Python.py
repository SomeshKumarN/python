"""Write a Python program to list all files in a directory in Python."""

#Solution:
from genericpath import isdir
import glob
import os
from tkinter.filedialog import Directory
from isort import file


directoryLocation = input("Give the directory location:")
if(isdir(directoryLocation)):
    #Way-1
    print(os.listdir(directoryLocation))
    
    #Way-2
    for s in os.scandir(directoryLocation):
        print(s.path)
        print(s.name)
    
    #Way-3
    print(glob.glob(directoryLocation))
else:
    print("Enter valid file location:")        