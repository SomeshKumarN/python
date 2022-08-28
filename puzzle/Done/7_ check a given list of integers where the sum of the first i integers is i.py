"""
Write a Python program to check a given list of integers where the sum of the first i integers is i.
Input:
[0, 1, 2, 3, 4, 5]
Output:
False
Input:
[1, 1, 1, 1, 1, 1]
Output:
True
Input:
[2, 2, 2, 2, 2]
Output:
False
"""
#solution
test = 1
def x(lst):
    global test
    print('\nTest---->',test)
    b = 0
    for i in range(len(lst)):
        b += lst[i]
    print(len(lst)==b)
    test+=1
x([0, 1, 2, 3, 4, 5])     
x([1, 1, 1, 1, 1, 1])     
x([2, 2, 2, 2, 2])     
