# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
def equal(num_1,num_2):
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        if num_1 == num_2 or num_1 + num_2 == 5 or abs(num_1 - num_2) == 5 :
            return True
        else:
            return False
    except:
        return "Invalid Input"
print(equal(5,5))
print(equal(-5,-5))
print(equal(10,5))
print(equal(-10,-5))
print(equal(2,3))
print(equal(-2,-3))
print(equal('',''))
print(equal(2.0,4.0))

