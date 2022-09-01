"""
Write a Python program find the longest string of a given list of strings.
Input:
['cat', 'car', 'fear', 'center']
Output:
center
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
shatter

"""
#solution

def x(a):
    # lst = []
    # for i in a:
    #     lst.append(len(i))
    # for i in a:
    #     if max(lst) == len(i):
    #         print(i) 
      
    b = dict()
    for i in a:
        b[i]=len(i)
    c = sorted(b.items())
    print(b)
    print(c)
b = ['cat', 'car', 'fear', 'center']
c =['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
x(b)
x(c)