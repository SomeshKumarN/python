"""Write a python program to get the path and name of the file that is currently executing."""

#Solution:
import os
print("Current executing file full path:\n",(__file__))
print("Current executing file's folder name:\n",os.path.basename(__file__))
print("Current executing file name:\n",os.path.basename(__file__))