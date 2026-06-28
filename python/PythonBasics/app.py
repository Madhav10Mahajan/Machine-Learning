print(1+1)

'''
hello this is a multiline comment 
'''

''' 
python is case sensitive language
'''
name='krish'
Name='naik'
print(name)
print(Name)

''' 
python uses indentation to define blocks of code
'''
age=32
if age>=30:
  print('inside if statement',age)
  
print('outside if statement',age)

age=32
height=4
name='madhav'

print('name: ',name)
print('height: ', height)
print('age: ', age)

# naming convention always start with letters or underscore and contain letters, numbers and underscore
# variable names are case sensitive

# valid variable names
first_name='madhav'
last_name='mahajan'

# invalid variable names
# first-name='madhav'
# @name='krish'

# understanding variable types
# python is dynamically typed language we dont need to explicity mention the dtata type of the variables
# data type is determined at run time

age=24 # number
name='madhav' # string
isValid=True # boolean

print(type(name))
print(type(age))
print(type(isValid))

height=5.11
print(type(height)) 

# age=int(input('what is your age'))
# print(age,type(age))


num1=int(input('enter your first number'))
num2=int(input('enter ypur second number'))

sum=num1+num2
diff=num1-num2
product=num1*num2
quotient=num1/num2

print('sum', sum)
print('product', product)
print('diff', diff)
print('quotient', quotient)

print('operators in python')
# operators in python
# arithmetic operators
# +, -, *, /, %, **, //
# addition, subtraction, multiplication, division, modulus, power, integer division

print(2+3)
print(3-4)
print(5*1)
print(4/3)
print(4%2)
print(2**3)
print(10//9) # floor division

# comparison operators
# ==, !=, >, <, >=, <=
print(2=='2') # False
print(2==2) # True
print(True==1) # True

# logical operators
# and, or, not  

# and both conditions or variables need to be true
# or either of them should be true
# not is used to negate the original value

x=True
y=False
print(x or y) # True
print(x and y) # False
print(not x) # False

# if else conditionals
# num=int(input('enter your num'))
# if num>0:
#    print('the number is positive')
# elif num==0:
#     print('the number is zero')
# else:
#    print('the number is negative')

for i in range(0,5):
    print(i)
    
for i in range(1,10,2): # third parameter is the step size
    print(i)
    
# break used to break the loop
# continue used to skip a particular iteration
# pass is a null operation it does nothing

for i in range(1,101):
    isPrime=True
    for j in range(2,i):
        if i%j==0:
            isPrime=False
            break
    if isPrime==True and i!=1:
        print(i, 'is a prime number')