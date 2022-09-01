"""
Write a Python program to check whether the given strings are palindromes or not. Return True, False.
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]






"""

#solution

def a(lst):
    result = []
    for i in range(len(a)):
        a = lst[i]
        if a[::-1] == a:
            result.append(True)
        else:
            result.append(False)     
    return result
x = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
print(a(x))       