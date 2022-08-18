"""Write a Python program to create a histogram from a given list of integers."""

#Solution:

test=1

def drawHistogram(size):
    global test
    print("\nTest--",test)
    for i in range(size+1):
        print('*'*i)
    test+=1


#Tests
drawHistogram(5)
drawHistogram(8)
drawHistogram(10)
drawHistogram(40)
