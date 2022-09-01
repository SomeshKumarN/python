"""
Write a Python program to find the strings in a given list, starting with a given prefix.
Input:
[( 'ca',('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[('do',('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
Output:
['dog', 'donut']

"""
#solution

def x(a):
    lst = []
    for i in range(len(a[0][1])):
        b = a[0][1][i]
        if a[0][0] in b[0:2]:
            lst.append(b)
    print(lst)        
lst_1 = [( 'ca',('cat', 'car', 'fear', 'center'))]
lst_2 =[('do',('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
x(lst_1)
x(lst_2)