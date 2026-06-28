# generators are easy way to create iterators, they use yeild keyword to produce a series of values lazily
# which means they generate values on the fly and do not store them in memory

def square(n):
    for i in range(n):
        yield i**2

print(square(3))

for i in square(3):
    print(i)

a=square(3)
print(a)
print(next(a))
print(next(a))
print(next(a))
# print(next(a)) StopIteration error
# useful for reading large files
# helps to read files without loading the entire text at once, uses chunks