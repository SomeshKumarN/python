"""
Write a Python program to check the nth-1 string is a proper substring of nth string in a given list of strings.
Input:
['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
Output:
True
Input:
['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
Output:
True
"""
#solution

def substr(lst):
    return lst[-2] in lst[-1]
x = ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
y = ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
z = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
h = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']   
print(substr(x))    
print(substr(y))    
print(substr(z))    
print(substr(h))    