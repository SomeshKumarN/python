# init method 

class store:
    snakce='bisciuts'

# create object for class
obj = store()

obj.snakce = "soda"

store.snakce="soda"

print(obj.snakce)

class store:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    @property    
    def details(self):
        print(self.name + " price is "+ str(self.price))    

product1=store("soap",20)
product2=store('sampoo',5)

product1.price()
print(product1.name)
print(product1.price)
product1.details