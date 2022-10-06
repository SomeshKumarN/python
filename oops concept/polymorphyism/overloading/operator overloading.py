"""# operator overloading
class operator:
    def __init__(self,a):
        self.a=a 

    def __add__(self,other):
        return self.a + other.a

    def __lt__(self,other):
        if self.a < other.a:
            return True
        else :
            return False

    def __gt__(self,other):
        if self.a > other.a:
            return True
        else :
            return False  

    def __sub__(self,other):
        return self.a - other.a  
         
    def __mul__(self,other):
        return self.a * other.a

obj = operator(30)
obj1 =operator(40)
print(obj < obj1) 
print(obj > obj1)        
print(obj - obj1)        
print(obj + obj1)  
print(obj * obj1)        
"""

class a :
    def __init__(self,a):
        self.a = a
        
    def __add__(self,emp,emp1):
        return emp.a + emp1.a 
    # def __sub__    

emp = a(100)
emp1 = a(200)
print(emp.__add__(emp,emp1))
# print(emp + emp1)
