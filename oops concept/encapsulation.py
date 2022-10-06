
class base:
    def __init__(self):
        self.__abc = 10
        
    def printer(self,input):
        self.__abc = input
        print(self.__abc)
class test(base):
    def printr(self):
        print(self.__abc)        
# obj = base()
# obj.printer(5)
# print(obj.__abc)
obj1 =test()
obj1.printr()


class base:
    def __test(self):
        print("print from test")
    def printer(self):
        self.__test()      
class c(base):
    def printerr(self):
        self.__test()
obj = base()
obj.printer()

# obj1 = c()
# obj1.printerr()