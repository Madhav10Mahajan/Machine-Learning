# ordered mutable list of items
# can contain items of different data types

list=[]
print(type(list))
names=['madhav','rahul','rohit','aman',1,3,4,5] # can have different data types
print(names)

# accessing list elements
names[0]
print(names[0])
names[0]='rohan'
print(names[0])   
print(names[1:3]) # starting from 1 till 3-1 (3 index not included)

fruits=['apple', 'mango','orange','cherry','litchi','chikoo','guava']
print(fruits[-1])

#list methods
fruits.append('pineapple')
print(fruits)

fruits.insert(1,'banana')
print(fruits)

fruits.remove('apple') # removes the first occurrence of 'apple'
print(fruits)

# removes and returns the last element of the list
last_fruit=fruits.pop()
print(fruits)
print(last_fruit)

print(fruits.index('cherry')) # gets index of the element
# print(fruits.index('apple')) # gives error apple not present in the list

print(fruits.count('banana')) # gives the count/freq of banana occuring in the list
fruits.append('banana')
print(fruits.count('banana'))

fruits.sort() # sort in ascending order
print(fruits)

fruits.append('apple')
fruits.sort()
print(fruits)

fruits.reverse()
print(fruits) #reverse the list fruits

fruits.clear() #removes all items clears the list
print(fruits)

numbers=[1,2,3,4,5,6,7,8,9]
print(numbers[2:5]) # elements from index 2 to 4 i.e 3, 4, 5
print(numbers[:5]) # all elments from start till the 5th index
print(numbers[5:]) # elemens aftet the 5th index till the last
print(numbers[::2]) # step size of 2 like i=2 in for loop
print(numbers[::-1]) # step size is 1 starting from the end 
print(numbers[::-2]) # step size is 2 from end

for (i,num) in enumerate(numbers): # to get index
    print(i,num)

# list comprehension
for x in range(10):
    list.append(x**2)
    
print(list)

a=[x**2 for x in range(10)]
print(a)
# [operation loop] [expression for item in iterable if condition]
b=[x**2 for x in range(10) if x%2==0]
print(b)

lst1=[1,2,3]
lst2=['a','b']
#nested list comprehension
#[expression for item1 in iterable1 for item2 in iterbale2]

list=[(i,j) for i in lst1 for j in lst2]
print(list)
print(len(list)) # length of the array/list 'list'