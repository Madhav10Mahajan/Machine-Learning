# encapuslation involves bundling data and methods that operate on data within a single unit
# data bundling where as abstraction is called data hiding/hiding the underlying complexity

# wrapping of methods and attributes within a single unit
# restricts direct access to certain variables/data memebers to prevent misuse of data
# can be implemented using setters and getters

# access specifiers 
# public, private and protected

class Person:
    def __init__(self,name,age): # public specifier
        self.age=age
        self.name=name
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
# by default all data members and methods ar public i.e they can be accessed outside the class aswell
person=Person('krish', 23)
print(person.name)
print(person.age)

print(dir(person))

# if I dont want the user to access certain variable outside the class
# for that we use protected and private variables

class Person:
    def __init__(self,name,age): # private specifier
        self.__age=age   # private variable
        self.__name=name # private variable
        
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
person=Person('krish',34)
name=person.getName()
age=person.getAge()
print(name,age)
# print(person.age) error you cant access these variables outside the class since these are declared as private  
# print(person.name) 

# protected variables cant also be access outside the class but they can be accessed by the derived classes
class Person:
    def __init__(self,name,age): # protected specifier
        self._age=age   # protected variable
        self._name=name # protected variable
        
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age

class Employee(Person):
    
    def __init__(self,name,age):
        super().__init__(name,age)

employee=Employee('krish',34)
print(employee._age)
print(employee._name) 

# encapsulation using getters and setters

class Person:
    def __init__(self,name,age):
        self.__age=age
        self.__name=name
    
    # getter for name
    def getName(self):
        return self.__name
    
    def setName(self,name):
        self.__name=name
    
person=Person('vedant',34)
print(person.getName())
person.setName('madhav')
print(person.getName())