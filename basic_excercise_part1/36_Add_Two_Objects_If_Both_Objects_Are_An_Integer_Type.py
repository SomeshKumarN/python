"""Write a Python program to add two objects if both objects are an integer type."""

#Solution:
def addTwoObjects(obj1, obj2):
    if(isinstance(obj1,int)):
        if(isinstance(obj2,int)):
            print("Result of (obj1+obj2) is-->",int(obj1)+int(obj2))
        else:
            print("Object2 is not a proper integer")
    else:
        print("Object1 is not a proper integer")

#Tests
addTwoObjects(4,4)
addTwoObjects(4,'4')
addTwoObjects('4',4)
addTwoObjects('4','4')