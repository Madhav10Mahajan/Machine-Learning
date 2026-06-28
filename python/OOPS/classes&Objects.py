# object oriented programming makes uses of classes and objects to implement real life scenarios into programm ing
# it is used to apply practical application to programming
# classes are like blue prints which have certain properties and functions
# an instance of a class is called object

class Car:
    pass

audi=Car()
bmw=Car()

print(audi) # car object at this specific memory location
print(type(audi)) # object

audi.windows=4
print(audi.windows) # 4
# print(bmw.windows) AttributeError: 'Car' object has no attribute 'windows'

class Dog:
    # constructor is used to initalize the object
    def __init__(self,name,age): 
        self.name=name # data members
        self.age=age

# creating an object
dog1=Dog('rocky',10)
print(dog1)
print('name: ',dog1.name,'age: ',dog1.age)

# defining a class with instance method or member functions
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def barking(self):
        print(f'{self.name} is barking')
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

dog=Dog('rick',10)
dog.barking()
name=dog.getName()
age=dog.getAge()
print(name,age)

# modeling a bank account

# define a class for bank account
class BankAccount:
    
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        
    def getBalance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"{amount} has been deposited to {self.owner}'s account, the remaining balance is {self.balance}")
    
    def withdraw(self,amount):
        if self.balance<amount:
            print('Insufficient balance')
        else:
            self.balance=self.balance-amount
            print(f"{amount} has been withdraw from {self.owner}'s account, the remaing balance is {self.balance}")
            
account1=BankAccount('madhav',100)
account1.deposit(200)
account1.withdraw(300)
print(account1.getBalance())
account1.withdraw(20)