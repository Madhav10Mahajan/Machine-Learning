# iterators allow efficiet looping and memory mgmt
# they provide a way to access elements of a collection sequentially without exposing the underlying structure

my_list=[1,2,3,4,5,6]

print(type(my_list))
# normal way of looping thru a list
for item in my_list:
    print(item, end=' ')
    
iterator=iter(my_list)
print(iterator)
print(type(iterator))

# iterate thur all the elements 
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) error stop iteratior

try:
    print(next(iterator))
except StopIteration:
    print('there are no elements left in the iterator')
    
my_string='Hello'

iterator=iter(my_string)
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print('there are no elements left in the iterator')