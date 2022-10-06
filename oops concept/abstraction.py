# Example one
from abc import ABC,abstractmethod
class messagingapp(ABC):
    @abstractmethod
    def message(self):
        pass
class whatsapp(messagingapp):
    def message(self):
        print("print from ")

class signal(messagingapp):
    def message(self):
        print("print from signal") 
class telegram(messagingapp):
    def message(self):
        print("print from telegram")

obj = telegram()
obj.message()

# Example two
class AbstractMotor(ABC):
    @abstractmethod #decorator
    def engine():
        pass
    @abstractmethod
    def rotor():
        pass
    @abstractmethod
    def coil():
        pass

class InheritanceMotor(AbstractMotor):
    def engine():
        print("from InheritanceMotor engine")
    def rotor():
        print("from InheritanceMotor rotor")
    def coil(): 
        print("from InheritanceMotor coil")

class newMotor(AbstractMotor):
    def newEngine(self):
        InheritanceMotor.engine()
        print("from newMotor")
    def engine():
        pass
    def rotor():
        pass
    def coil():
        pass
obj = newMotor()
obj.newEngine()

obj1 = newMotor()
newMotor.newEngine()