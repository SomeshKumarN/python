"""
Write a Python program to accept a filename from the user and print the extension of that. 

Sample filename : abc.java

Output : java
"""

#Solution:
from fileinput import filename


fileName = input("Enter fileName:")
print("Extention of the provided file is",fileName.split('.')[-1])