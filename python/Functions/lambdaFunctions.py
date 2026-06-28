# lambda functions are anonymous functions i.e dont have a name
# defined using lambda keyword
# used for short operations or as arguments to higher order functions

# syntax lambda arguments: expression
 
def addition(a,b):
    return a+b

print(addition(2,3))  # 5

addition=lambda a,b: a+b
print(addition(2,3))
print(type(addition)) 

def even(num):
    return num%2==0

lambda num:num%2==0

print(even(3))

numbers=[1,2,3,4,5]

def square(num):
    return num*num

lst=[]
for item in numbers:
    lst.append(square(item))
    
ans=list(map(lambda x:x**2,numbers))
print(ans)

# map function similar to map in js it is used to apply a particular function to all elements of an array/list
square= lambda x:x**2
numbers=[1,2,3,4,5]
ans=list(map(square,numbers))
print(ans)

# lambda function with map

numbers=[1,2,3,4,5]
ans=list(map(lambda x:x**2, numbers))
print(ans)

numbers1=[1,2,3]
numbers2=[4,5,6]

added_numbers=list(map(lambda x,y:x+y,numbers1,numbers2))
print(added_numbers)

# convert list of strings to integers

strings=['1', '2','3', '4', '5']
print(list(map(lambda s:int(s), strings)))

def get_name(persons):
    ans=[]
    for person in persons:
        ans.append(person['name'])
    
    return ans
    

persons=[{'name':'madhav', 'age':23},{'name':'rohit', 'age':23},{'name':'rohan', 'age':23}]
ans=get_name(persons)
print(ans)

# using map function
def get_name_2(person):
    return person['name']
    
print(list(map(get_name_2,persons)))
print(list(map(lambda person:person['name'],persons)))
