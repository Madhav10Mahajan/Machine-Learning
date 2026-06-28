#dictionaries
# unordered collection of items stores data in key value pairs
# similar to objects having key value pairs
# keys must be unique and immutable 

empty_dict={}
print(type(empty_dict))
print(empty_dict)

student={"name":"Krish", "age":32, "grade":24}
print(student)
student={"name":"Krish", "age":32, "grade":24, "name":'mahajan'}
# overwrites the name key
print(student)

# accessing dictionary elements
print(student['grade']) # 24
print(student['age']) # 32

# using get method inbuilt method of dictionary

print(student.get('grade'))
print(student.get('name'))
print(student.get('last_name')) # None
print(student.get('last_name', 'Not Available')) # Not Available


# modifying dictionary elements
# dictionaries are mutable so we can add, update, remove elements
# keys need to be unique

print(student)
student['age']=33 # updating existing key
student['last_name']='rohan' # adding new value
print(student)

del student['name'] # deleting key and value pair
print(student)

# dictionary methods commonly used

keys=student.keys()
values=student.values()
print('keys: ', keys) # gets all the keys
print('values: ', values) # gets all the values

print(student.items()) # key value pairs

# shallow copy
student_copy=student
print(student)
print(student_copy)

# modifying one will cause change in the other since both point to the same address
student_copy['age']=34
print(student)
print(student_copy) 

student_copy=student.copy()
student['first_name']='rohit'
print(student)
print(student_copy)

# iterating over dictionaries using loops

for key in student:
    print('key: ',key,',', 'value: ', student[key])

for key,value in student.items():
    print(f"{key}:{value}")

# nested dictionaries

students={
    'student1':{'name':'krish', 'age':21},
    'student2':{'name':'peter', 'age':32}
}
print(students)

# access nested dictionaries
print(students['student1']['name']) # krish
print(students['student2']['age']) # 32

# iterating over nested dictionaries
for keys in students.keys():
    print(f'{keys}', end=' ')
    for key in students[keys].keys():
        print(f'{key}:{students[keys][key]}', end=' ')
    print()

# dictionary comprehension
squares={x:x**2 for x in range(10)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5:

# use dictionary to count frequency of elements in a list
numbers=[1,2,2,21,1,1,23,2,11,1]
dict={}
for item in numbers:
    if item in dict:
        dict[item]=dict[item]+1
    else:
        dict[item]=1

print(dict)

# merge 2 dictionaries
dict1={"a":1, "b":2}
dict2={"c":1, "d":2}

merged_dict={**dict1,**dict2}
print(merged_dict)
