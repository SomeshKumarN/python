# Write a Python program to sum of three given integers.
# However, if two values are equal sum will be zero.
def fun(num_1,num_2,num_3):
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        num_3 = int(num_3)
        if num_1 == num_2 or num_2 == num_3 or num_1 == num_3:
            sum = 0
        else:
            sum = num_1 + num_2 + num_3
        print("sum three numbers is :", sum)
    except:
        print("Invalid Input")
       
fun(3,4,5)
fun(5,7,5)
fun(-5,7,-5)
fun(-5,7,5)
fun(-5,-6,-7)
fun('s','h','i')
fun(-3,6,-5)
fun('3','4','5')





