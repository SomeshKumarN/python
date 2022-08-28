"""
Write a Python program that accept an integer test whether an integer greater than 4^4 
and which is 4 mod 34.
Input:
922
Output:
True
Input:
914
Output:
False
Input:
854
Output:
True
Input:
854
Output:
True
"""
#solution
test = 1
def call(a):
    global test 
    print('\nTest------>',test)
    test+=1
    return a > 4**4 and a % 34 == 4
            
print(call(922))        
print(call(914))        
print(call(854))        
       
