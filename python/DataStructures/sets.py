# sets are builtin data types in python used to store unique items
# they dont contain duplicates

# creating a set
my_set={1,2,3,4}
print(my_set)
print(type(my_set))

print(set())

my_set=set([1,2,4,5,3,2,1])
print(my_set) # dont contain duplicates

# sets dont contain any specific order of elements

# adding and removing elements in set

my_set.add(7)
my_set.remove(2)
print(my_set)

# my_set.remove(10) will raise KeyError if 10 is not present
my_set.discard(10) # will not raise error if 10 is not present

# pop method
removed_element=my_set.pop() # removes and returns a random element from the set
print(removed_element)

# clear method
my_set.clear() # removes all elements from the set
print(my_set)

# membership testing
# used to test whether a number is present in the set or not

my_set={1,2,3,4,5}
print(3 in my_set) # True
print(6 in my_set) # False

set1={1,2,3}
set2={6,4,5}
union=set1.union(set2) # combination of both elements
print(union)

intersection=set1.intersection(set2) # common elements
print(intersection)

set1.intersection_update(set2) # whatever are the common lements they get updated inside set1

print(set1)

set1={1,2,3}
set2={3,4,5}
print(set1.difference(set2))
# print(set1.difference_update(set2)) updates set1 with difference set1-set2

print(set1.symmetric_difference(set2)) # removes the intersection elements i.e the common elements from both of them and then take the union 

# set methods

set1={1,2,3}
set2={3,4,5}

print(set1.issubset(set2)) # False
print({2}.issubset({3,2})) # True

print({1,2}.issuperset({3})) # False

print({1,2}.isdisjoint({4,5})) # True

# removing duplicates
numbers=[1,2,3,4,4,3,2,21,21,1,1,34]
s=set({})
for item in numbers:
    s.add(item)

numbers.clear()
print(s)
for item in s:
    numbers.append(item)

print(numbers)

# counting unique words in text
text="in this tutorial we are discussing about sets"
words=text.split()
print(words)

unique_words=set(words)
print(unique_words)