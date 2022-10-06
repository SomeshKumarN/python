
class abc :
    def fun(self,a):
        print(a)
    def fun(self,a,b):      # ------> this type method is not avilable for python
        print(a+b)
    def fun(self,a,b,c):
        print(a+b+c) 

# alter methods
class abc :
    def fun(self,a=0,b=0,c=0):
        print(a+b+c)

class abc :
    def fun(self,*a):
        s = 0
        for i in a:
            s+=i
        print(s)

class abc:
    
    def fun1(self,*agr):
            
        if type(agr[0]) == int:
            e =  0
        elif type(agr[0]) == str:
            e = ''  
        elif type(agr[0]) == float:
            e = 0.0      
        
        for i in agr:
            e = e + i
        print(e)

obj  = abc()
obj.fun1(7) 
obj.fun1("Im ",'a ','boy')
obj.fun1(68.8,87.9)                  