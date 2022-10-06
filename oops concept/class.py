class oops:
    a = 5
    def fun(self):
        print("print function")


# This is object(obj)
obj = oops()
obj.fun()

# print class variable
print("print the variable in dot notation :",obj.a)
print("print in getattr method :" ,getattr(obj,'a'))

# This method handling the errors
print("error handling by getattr :",getattr(obj,'b','No found'))

# set new variable and variables in class
setattr(obj,'name',"som")
# another one method of set variable and values 
obj.age=20

print(getattr(obj,"age",'no found'))
print("check the name variable :",obj.name)
print("check in getattr method :",getattr(obj,"name"))

# DELETE VARIABLE METHODS
delattr(obj,'name')

# ANOTHER ONE METHOD OF DELETE
#del(obj.name)
print(getattr(obj,"name","ERROR"))