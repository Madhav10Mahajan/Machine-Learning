# ordered collection of immutable items
# can contain items of different data types

empty_tuple=()
print(empty_tuple)
print(type(empty_tuple)) # tuple

my_list=[]
print(type(my_list)) # list

x=tuple()
print(x)

numbers=tuple([1,2,3,4,5])
print(numbers)

lst=list((1,2))
print(lst)

# you can convert tuple to list and list to tuple as well
mixed_tuple=(1,'hello world', True,4.4)
print(mixed_tuple)

print(mixed_tuple[0])

print(numbers[0:4])
print(numbers[::-1]) # step size 1 starting from the end

print(numbers+mixed_tuple) # concatenation of tuples

# tuples are immutable i.e you cant modify them
list=[1,2,3,4]
list[1]='krish'
print(list)
# temp=tuple((1,2,3,4)) # gives error tuples dont support item assignment
# temp[1]='krish'
# print(temp)

print(numbers.count(1)) # gives the count of 1
print(numbers.index(3)) # gives the first index of the value 3


# packing and unpacking tuple

packed_tuple=1,'hello',3.14 # by default comma separated values are considered tuple (packing a tuple)
a,b,c=packed_tuple # unpacking a tuple
print(a,b,c) 

# unpacking with *
first,*middle,last=numbers 
print(first,middle,last) # [1, [2,3,4], 5]

# nested tuple

lst=[[1,2,3],[5,6,'hello'],[8,True,'madhav']]
print(lst)
lst=tuple(lst)
print(lst)
print(lst[0][2]) # lst[0]=[1,2,3] lst[0][2]=3

nested_tuple=((1,2),(3,4,'madhav'))
print(nested_tuple[0][1])
print(nested_tuple[1])

# iterating over nested tuples
for tuple in nested_tuple:
    for item in tuple:
        print(item, end=" ") 
    print()

# cant append or remove items from tuple sicne these are immutable