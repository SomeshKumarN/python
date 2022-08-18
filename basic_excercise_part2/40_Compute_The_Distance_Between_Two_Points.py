"""Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)."""

#Solution:

from math import sqrt

def getDistance(x1:int, y1:int, x2:int, y2:int):
    #formula for distance is d=√((x2 – x1)² + (y2 – y1)²)
    return sqrt(pow((x2-x1),2)+pow((y2-y1),2))


_inp = list(map(int, list(input("Enter (x1, y1) and (x2, y2):").split(','))))
print("distance -->",getDistance(_inp[0],_inp[1],_inp[2],_inp[3]))