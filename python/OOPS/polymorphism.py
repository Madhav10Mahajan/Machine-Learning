# another important pillar of oops
# poly means many and morphism means form so many forms
# it allows to perform different operations using the same function name
# allows an object to perform a single action in different forms
# achieved thru method overriding and interfaces  

# method overriding the child class overrides a particular method which has already been defined in the parent class
class Animal:
    
    def speak(self):
        return "Sound of the animal"

class Dog(Animal):
    def speak(self): # method overriding
        return "Woof"

class Cat(Animal):
    
    def speak(self): # method overriding
        return "Meaow"

def animal_speak(animal):
    return animal.speak()

dog=Dog()
animal=Animal()
cat=Cat()
print(animal.speak())
print(cat.speak())
print(dog.speak())
print(animal_speak(dog))

# polymorhism with functions and methods
# base class
class Shape:
    
    def area(self):
        return "return the area of the figure"

# derived class 1
class Rectangle(Shape):
      
    def __init__(self,width,length):
          self.width=width
          self.length=length
          
    def area(self):
        return self.length*self.length

# derived class 2

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius*self.radius
    
def print_area(shape):
    print(f'the area of the shape is {shape.area()}')

rectangle=Rectangle(4,5)
circle=Circle(4)
print_area(circle)
print_area(rectangle) 

# polymorphism with abstract base class (ABC)
# are used to define common methods for a group of related objects
# they can enforce that derived classes implement particular methods, promoting consistency across different implementations
from abc import ABC,abstractmethod

#define an abstract class empty class/empty method the derived classes would define the method 
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# derived class 1
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

# derived class 2
class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started"

bike=Bike()
car=Car()

def start_vehicle(vehicle):
    return vehicle.start_engine()

print(start_vehicle(bike))
print(start_vehicle(car ))
