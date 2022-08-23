"""
Write a Python program that accept a list of integers and check the length and the fifth element. Return true if the length of the list is 8 and fifth element occurs thrice in the said list.
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False
Input:
[11, 12, 14, 13, 14, 13, 15, 14]
Output:
True
Input:
[19, 15, 11, 7, 5, 6, 2]
Output:
False
"""
#solution
test = 1
def lst(a):
    global test
    print('Test--->',test)
    b = a[4]
    if len(a) == 8 and a.count(b) == 3:
        print(True)
    else:
        print(False)    
    test += 1       
lst([19, 19, 15, 5, 5, 5, 1, 2])
lst([19, 15, 5, 7, 5, 5, 2])
lst([11, 12, 14, 13, 14, 13, 15, 14])
lst([19, 15, 11, 7, 5, 6, 2])