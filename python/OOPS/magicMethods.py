# magic methods also known as dunder methods are double underscore methods,
# special methods start and end with __, they help us to define behaviour of objects for built in operations,
# such as arithmatic, comparisons etc
# some commong magic methods are 


# __init__ constructor used to initalize an object
# __str__ string representation of an object
# __len__ len of object

class Person:
    pass

person=Person()
print(dir(person))

## basic magic methods

class Person:
 def __init__(self,name,age):
    self.name=name
    self.age=age
 def __str__ (self):
     return f"{self.name},{self.age} years old"
 def __repr__(self):
     return f"Person name is {self.name}, age: {self.age}"
 

person=Person('krish',34)
print(person)
print(repr(person))