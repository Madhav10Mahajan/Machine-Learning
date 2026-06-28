# inheritance is one of major pillar of oops
# in this concept a class derives certain properties and functions from the parent class
# just like a parent child relationship where children inherit certain behavior from their parents

class Car:
    
    def __init__(self,windows,doors,engineType):
        self.windows=windows
        self.engineType=engineType
        self.doors=doors
        
    def drive(self):
        print(f'the person will drive the {self.engineType} car')
    
car1=Car(4,5,'petrol')
car1.drive()

class Tesla(Car):
    
    def __init__(self,windows,doors,engineType,isSelfDriving):
        super().__init__(windows,doors,engineType) # calling the init method from the parent class
        self.isSelfDriving=isSelfDriving
    
    def selfDriving(self):
        print(f'Tesla supports self driving: {self.isSelfDriving}')

tesla1=Tesla(4,5,'electric',True)
tesla1.selfDriving()
tesla1.drive() # can use the methods of parent class
# the above was an example of single level inheritance

# multiple inheritance 
# when a class inherits from more than one base class
# Base Class1 
class Animal:
    
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        print('Subclass must implement this method')

# base class2
class Pet:
    
    def __init__(self,owner):
        self.owner=owner

# derived class
# inherits both animal and pet class

class Dog(Animal,Pet):
    
    def __init__(self,name ,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
    
    def speak(self):
        print(f'{self.name} says woof')


dog=Dog('rocky','madhav')
dog.speak() # overrides the speak method of the parent class
# first it searches in the child class if no speak method is found then searches in the parent classu