# Write a Python program to determine profiling of Python programs.
import time,cProfile
starttime = time.time()
# def b():
#     print('Hi')
#     print('vishnu')
#     print('bye')
#     print('thanks')
# b()   
a = print('tata')
endtime = time.time() 
print(endtime - starttime)
# another method 
print(cProfile.run('a'))

