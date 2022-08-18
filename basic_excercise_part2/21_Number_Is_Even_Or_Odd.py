"""Write a Python program to find whether a given number (accept from the user)
 is even or odd, print out an appropriate message to the user."""

#Solution:

test=1

def oddOrEven(number):
    global test
    print("\nTest--",test)
    try:
        if number%2 == 0:
            print("Given number is Even number")
        else:
            print("Given number is Odd number")
    except:
        print("Enter only integer value(Number)")
    test+=1

#Test
oddOrEven(4)
oddOrEven(1)
oddOrEven(-6)
oddOrEven(-3)
oddOrEven(True)
oddOrEven('s')
oddOrEven('somesh')
oddOrEven(0)
oddOrEven('')