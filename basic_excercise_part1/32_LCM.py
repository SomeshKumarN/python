"""Write a Python program to get the least common multiple (LCM) of two positive integers."""

#Solution:

test=1

def GCD(_list:list):
    global test
    # print("\nTest-->",test)
    gcdList=[]
    for val in _list:
        templist=[]
        for i in range(1,val+1):
            if(val%i==0):
                templist.append(i)
        gcdList.append(templist)
        print(gcdList)
    gcdSet={}
    for gcd in gcdList:
        if gcd == gcdList[0]:
            gcdSet = set(gcd)
        gcdSet.intersection_update(set(gcd))
    print("The GCD for the give numbers-",_list,"is",max(gcdSet))
    test+=1
    return max(gcdSet)    


def LCM(_list):
    global test
    print("\nTest--",test)
    product=1
    for i in range(len(_list)-1):
        lcm = _list[i]
        product=int(lcm) * int(_list[i+1])
        lcm = int(product/GCD(_list[i:i+1].copy()))
        print("The LCM for the give numbers-",_list,"is",lcm)

#Tests
LCM([5,10])
LCM([5,12])
LCM([5,12,60])