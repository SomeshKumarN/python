# Write a python program to get the path and name of the file that is currently executing.
from os import path
print(path.realpath(__file__))