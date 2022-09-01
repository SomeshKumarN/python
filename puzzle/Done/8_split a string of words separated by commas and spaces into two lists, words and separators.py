"""
Write a Python program to split a string of words separated by commas and spaces into two lists,
words and separators.
Input: W3resource Python, Exercises.
Output:
[['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
Input: The dance, held in the school gym, ended at midnight.
Output:
[['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
Input: The colors in my studyroom are blue, green, and yellow.
Output:
[['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]
"""

#solution
import re
input = 'W3resource Python, Exercises.'
slpt = re.split('([ |,]+)',input)
print(input)
print(slpt)
print([slpt[::2],slpt[1::2]])
