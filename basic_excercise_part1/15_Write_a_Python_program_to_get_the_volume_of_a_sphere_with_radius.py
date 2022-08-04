"""
Write a Python program to get the volume of a sphere with radius 6.
"""

#Solution:

from math import pi


radius = int(input("Enter radius of the spear:"))
volume = 1.33 * pi * pow(radius,3)
print("Volume of the spear is:",volume)