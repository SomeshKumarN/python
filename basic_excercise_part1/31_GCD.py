"""Write a Python program to compute the greatest common divisor (GCD) of two positive integers."""

#Solution:

test =1

def GCD(_list:list):
    global test
    print("\nTest-->",test)
    gcdList=[]
    for val in _list:
        templist=[]
        for i in range(1,val+1):
            if(val%i==0):
                templist.append(i)
        gcdList.append(templist)
        # print(gcdList)
    gcdSet={}
    for gcd in gcdList:
        if gcd == gcdList[0]:
            gcdSet = set(gcd)
        gcdSet.intersection_update(set(gcd))
    print("The GCD for the give numbers-",_list,"is",max(gcdSet))
    test+=1
    return max(gcdSet)    


#Tests
GCD([2,10])
GCD([6,12])
GCD([24,36])
GCD([18,24])

        

