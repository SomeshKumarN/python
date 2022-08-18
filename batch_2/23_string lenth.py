# Write a Python program
# To get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.
def mul(a,n):
#a = input("Enter a string :")
    #n = int(input("Enter number :"))
    try:    
        c = len(a)
        if c < 2:
            print(a*n)
        else:
            print((a[0]+a[1])*n)
    except:
        print("string only accept") 
    finally:
        print("Try again")


#Positive Tests  
mul('somnath',5)
mul('ab',5)
mul('a',5)
mul('',5)

#Negative Test
mul(True,5)
mul(5,'a')
# vishnu vi*n
# ab ab*n
# a a*n
# " " *n