# used to filter elements from an interable using the specified condition
# similar to filter function in js

def even(num):
    return num%2==0

print(even(2))

lst=[1,2,3,4,5,32,21,4,2]
print(list(filter(even,lst)))

# filtert with lambda function
print(list(filter(lambda x:x%2==0,lst)))

numbers=[1,2,3,434,54,23]
# even and greater than five
print(list(filter(lambda x:x%2==0 and x>5,numbers)))

# filter on dictionaries

persons=[{'name':'madhav', 'age':23},{'name':'rohit', 'age':23},{'name':'rohan', 'age':23}]

print(list(filter(lambda person:person['age']>=24,persons)))

# filter(function, argument/iterable) return elements which return true when function is applied on them
# map(function, argument/iterbale) applies function on all elements of the iterable

# function(a,b,c)=>function(a)(b)(c)
def multiply(a,b,c):
    return a*b*c

def multiply2(a):
    def inner(b):
        def final(c):
            return a*b*c
        return final
    return inner

print(multiply(1,2,3))
print(multiply2(1)(2)(3))

print(5/2)

def remove_duplicates(numbers):
    map={}
    for num in numbers:
        map[num]=map.get(num,0)+1
        
    ans=[]
    print(map)
    for key,value in map.items():
        if value==1:
            ans.append(key)
    
    return ans

print(remove_duplicates([1,2,21,1,3,42,21,123,4,4,322]))

def check_unique(lst):
    my_set=set()
    for item in lst:
        my_set.add(item)
    
    return len(my_set)==len(lst)

print(check_unique([1,2,3,4,5]))
print(check_unique([1,2,3,4,4,5]))

def reverse_list(lst):
    
    last_index=len(lst)-1
    ans=[]
    while last_index>=0:
        ans.append(lst[last_index])
        last_index=last_index-1
    
    return ans

print(reverse_list([1,2,3,4,5]))

def count_even_odd(lst):
    
    even=0
    odd=0
    for item in lst:
        if item%2==0:
            even=even+1
        else:
            odd=odd+1
    
    return tuple((even,odd))

print(count_even_odd([1,2,3,21,34,21,1]))

def is_subset(lst1,lst2):
    
    my_set=set()
    for item in lst2:
        my_set.add(item)
    
    for item in lst1:
        if item not in my_set:
            return False
    
    return True

print(is_subset([1,2,1],[3,4,42,21,1,1]))
            
def max_diff(lst):
    
    maxi=-1e9
    for i,item in enumerate(lst):
        if(i==len(lst)-1):
            break
        
        num1=lst[i]
        num2=lst[i+1]
        diff=abs(num1-num2)
        maxi=max(maxi,diff)
    
    return maxi

print(max_diff([1, 7, 3, 10, 5]))

def merge_two_sorted_list(lst1,lst2):
    
    ans=[]
    i=0
    j=0
    while i<len(lst1) and j<len(lst2):
        
        if lst1[i]<=lst2[j]:
           ans.append(lst1[i])
           i=i+1
        else:
            ans.append(lst2[j])
            j=j+1
    
    while i<len(lst1):
        ans.append(lst1[i])
        i=i+1
    
    while j<len(lst2):
        ans.append(lst2[j])
        j=j+1
    
    return ans

print(merge_two_sorted_list([1,3,5],[2,4,6]))
                    
def rotate_list(lst,k):
    length=len(lst)
    if k==0 or k%length==0:
        return lst
    
    rem=k%length
    index=length-rem
    temp1=lst[0:index]
    temp2=lst[index:]
    print('part 1',temp1)
    print('part 2',temp2)
    temp=temp2+temp1
    return temp

print(rotate_list([1,2,3,4,5],0))

def merge_lists_into_dictionaries(keys,values):
    if len(keys)!=len(values):
        return -1
    
    ans={}
    index=0
    while index<len(keys) and index<len(values):
        ans[keys[index]]=values[index]
        index=index+1
    
    return ans

print(merge_lists_into_dictionaries(['a','c'],[1,2,3]))
    
def merge_n_dictionaries(arr):
    length=len(arr)
    ans={}
    for obj in arr:
        for key,value in obj.items():
            ans[key]=value
    
    return ans

print(merge_n_dictionaries([{'a':1,'b':2},{'c':3, 'd':4},{}]))

def is_palindromic(tup):
    
    length=len(tup)
    lst=list(tup)
    start=0
    end=length-1
    while start<=end:
        if lst[start]!=lst[end]:
            return False
        
        start=start+1
        end=end-1
    
    return True

print(is_palindromic((1,2,3,3,2,1)))

def merge_dicts_with_overlapping_keys(dicts):
    
    length=len(dicts)
    ans={}
    for dict in dicts:
        for key,value in dict.items():
            ans[key]=ans.get(key,0)+value
            
    return ans

print(merge_dicts_with_overlapping_keys([{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]))