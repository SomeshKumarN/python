# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
def gcd(num_1,num_2):
    try:  
        #i = list(map(int, input("Enter two numbers with comma seperated :").split(",")))

        
        a = abs(num_1)
        b = abs(num_2)
        divisors_1 = []
        divisors_2 = []
        for i in range(1, a+1):  #range(1,0) -10/5   10/5

            if a % i == 0:
                divisors_1.append(i)
        for i in range(1, b+1):
            if b % i == 0:
                divisors_2.append(i)
        print(divisors_1)
        print(divisors_2)        
        set_1 = set(divisors_1)
        print(set_1)
        set_2 = set(divisors_2)
        print(set_2)
        c = set_1.intersection(set_2)
        print(max(c))
    except:
        print("Invalid Input\nInteger values only accepted with comma seperated")
    finally:
        print("Thank you")


#gcd(9,10)
#gcd('d','s')

#gcd(7.3,5.6)
#gcd(-1,-4)
gcd(-3,3)



# 10 --> 1 , 2, 5, 10
# 9 ---> 1, 3 , 9      

# divisors_1 --> 