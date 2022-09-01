"""
Write a Python program to find the lengths of a given list of non-empty strings.
Input:
['cat', 'car', 'fear', 'center']
Output:
[3, 3, 4, 6]
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
[3, 3, 7, 5, 2, 4, 0]

"""
#solution
def x(a):
    length = []
    for i in a:
        length.append(len(i))
    print(length)    
a = ['cat', 'car', 'fear', 'center']
b = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
x(a)
x(b)