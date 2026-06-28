# function definition, calling, arguments, parameters
# it is a block of code that performs a specific task, helps it organizing code, reusing code and readabilty

# format of a function
# def function_name(parameters):
#     """Docstring"""
#     return expression

def evenOrOdd(num): # checks whether a num is even or odd
    return num%2==0

print(evenOrOdd(2)) # True
print(evenOrOdd(3)) # False
# evenOrOdd func can now be used anywhere throughout the project

# function with multiple parameters

def add(a,b):
    c=a+b
    return c

print(add(3,4)) # 3+4=7

# default parameters
def greet(name='rohan'): #default parameter rohan if name is not provided
    print(f"Hello {name}")

greet('madhav')
greet()

# variable length arguments
# postion and keyword arguments

# postional argument
def print_numbers(*args):
    for num in args:
        print(num, end=" ")
        
print_numbers(1,2,3,34,43,3)
print()


# keywords argument
def print_details(**args): # all the parameters will in the form of key value pairs
    for key,value in args.items():
        print(f"{key}:{value}")

print_details(name='madhav', age=23, height=6.0)

# return statement
def square(num):
    return num**2,num

print(square(4)) # 16

def temp_conversion(temp,unit):
    """this function converts temp from celsius to farenhite and vice versa"""
    if unit=='C':
        return temp*9/5+32
    elif unit=='F':
        return (temp-32)*5/9
    else:
        return None

print(temp_conversion(25,'C'))
print(temp_conversion(77,'F'))


def password_strength_checker(password):
    """this function checks strength of the password"""
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True

def calculate_shopping_cart_cost(cart):
    ans=0
    for item in cart:
        ans=ans+item['cost']*item['quantity']
    
    return ans

cart=[{'name':'apple', 'cost':13,'quantity':50},{'name':'orange', 'cost':32,'quantity':15},{'name':'banana', 'cost':10,'quantity':5}]
print(calculate_shopping_cart_cost(cart))

def isPalindrome(s):
    
    s=s.lower().replace(" ","")
    start=0
    end=len(s)-1
    while start<=end:
        if s[start]!=s[end]:
            return False
        start=start+1
        end=end-1
        
    return True

print(isPalindrome('aabbaa')) # True
print(isPalindrome('aabbaxa')) # False

def factorial(n):
    
    if n==0 or n==1:
        return 1
    
    return n*factorial(n-1)

print(factorial(5))

def count_word_frequency(file_path):
    word_count={}
    with open(file_path,'r') as file:
        for line in file:
            words=line.split()
            for word in words:
                word=word.lower().strip('./;"+-:?/\|')
                if word in word_count:
                    word_count[word]=word_count[word]+1
                else:
                    word_count[word]=1
    
    return word_count

import os
filepath = os.path.join(os.path.dirname(__file__), 'sampleText.txt')
print(count_word_frequency(filepath))

