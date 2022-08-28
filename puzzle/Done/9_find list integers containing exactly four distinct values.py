
"""
Write a Python program to find list integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first twenty entries.
Input:
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
Output:
True
Input:
[1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
Output:
False
Input:
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
Output:
False
"""

test = 1
def find(a):
    global test
    print('\nTest----->',test)
    test+=1
    # find the distinct values of the list. duplicate values not allowed for set. so, we use set
    st = set(a)
    # first condition list integers containing exactly four distinct values. so, check length of set is 4         
    if len(st) == 4:
        # second condition no integer repeats twice consecutively.
        for i in range(len(a)-1):
            # compare sencond value to first value. 
            if a[i] != a[i+1]:
                #if sencond and first values are not equal it.ignore it and continue.
                continue
            # but if equal it return false 
            else:
                return False
        # if conditions are satisfy, return true        
        return True 
    # if conditions are not satisfy, return false    
    else:
        return False    
                               
x = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
y = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
z = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
a = [20, 10, 40, 40, 10, 40, 30, 40, 10, 30, 20, 40, 10, 20, 30, 40]
print(find(x))
print(find(y))
print(find(z))
print(find(a))
