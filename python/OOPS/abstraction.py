# abstraction is the concept of hiding the complex information and showing only the neceesary info to the user
# this helps in reducing programming complexity and effort

# real world examples like internal working of car engine or washing machine 
from abc import ABC,abstractmethod

# abstract base class
class Vehicle(ABC):
    def drive(self):
        print('the vehicle is used for driving')
    
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    
    def start_engine(self):
        print('the car engine started')
    
    
def operate_vehicle(vehicle):
    vehicle.start_engine()

car=Car()
operate_vehicle(car)