# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 

import math
def distance(x1,y1,x2,y2):
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2) # math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    return d
print(distance(x1=4, y1=0, x2=6, y2=6))





