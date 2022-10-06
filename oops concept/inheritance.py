# single inheritance

"""
class father:
    def ches(self):    
        print("playing chess")
class son(father):
    def cricket(self):
        print('play cricket')
sonhabits=son()
sonhabits.cricket()
sonhabits.ches()
"""  

# multiple inheritance

"""
class father:
    def chess(self):    
        print("play chess")
class mother :
    def cook(self):
        print('cook')        
class son(father,mother):
    def sonhabit(self):
        print('play cricket')        
habit=son()
habit.sonhabit()
habit.chess()
habit.cook()
"""

# multilevel inheritance

"""
class grandfather:
    def grandfatherproperty(self):
        print('5 acre')
class father(grandfather):
    def fatherproperty(self):
        print('2 acre')
class son(father):
    def sonproperty(self):
        print('no land')                
property = son()
property.grandfatherproperty()
"""   

# hierarchical inheritance

"""
class get:
    def getinput(self):
        self.a = int(input("enter a number"))
        self.b = int(input("enter b number"))
class add(get):
    def addtion(self):
        self.getinput()
        print(self.a + self.b)         
class sub(get):
    def subraction(self):
        self.getinput()
        print(self.a - self.b)
add = add()  
add.addtion()
sub = sub()
sub.subraction()
"""

# hybrid inheritance

"""class get:
    def getinput(self):
        self.a = int(input("Enter a value :"))
        self.b = int(input("Enter b value :"))

class add(get):
    def addtion(self):
        self.getinput()
        print("Addition Number :",self.a + self.b)         
class sub(get):
    def subtraction(self):
        self.getinput()
        print("Subtraction Number :",self.a - self.b)
class arith(add,sub):
    def arithmetic(self):
        self.addtion()
        self.subtraction()

obj = arith()
obj.arithmetic()"""
