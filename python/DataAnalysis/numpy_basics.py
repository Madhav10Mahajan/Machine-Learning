# numpy is the fundamental library in python, it provieds suport for arrays, matrcies along with collection
# of mathematical functions to operate on these data structures
import numpy as np
arr1=np.array([1,2,3,4])
print(arr1)
print(type(arr1))
print(arr1.shape)

arr2=np.array([3,4,5,5,6])
print(arr2)
print(type(arr2))
print(arr2.reshape(1,5)) # reshape the array to 1 row and 5 columns 
print(arr2.reshape(5,1)) # reshape the array to 5 rows and 1 column

arr2=np.array([[1,2,3,4,5], [5,4,3,2,3],[54,42,0,2,12]])
print(arr2.shape) # (3,5) 3 rows and 5 columns

print(np.arange(0,10,2).reshape(1,5)) # arrange is used to create an array containg elements from 0 to 10 with a step size of 2

print(np.ones((3,4))) # 3 rows and 4 cols with all elements as 1, it takes a tuple as argument

print(np.eye(3)) # identity matrix of zie 3X3

## numpy vectorized operations
arr1=np.array([1,2,3,4,5])
arr2=np.array([10,20,30,40,50])

## element wise addtion

print('Additon: ',arr1+arr2) # elements at same indices get added up
print('Subtraction: ', arr1-arr2) # elements at same indices get subtracted
print('Multiplication: ', arr1*arr2)

arr=np.array([1,2,3,4,5])
print(np.sqrt(arr)) # sqrt of each element
print(np.exp(arr)) # e^arr[i] 
print(np.log(arr)) # log of all elements

## array slicing 

arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(arr)

for row in arr:
    for element in arr:
        print(element,' ')
    print()

print(arr[0][0]) # 0th row and 0th col
print(arr[2][3]) # 2nd row and 3rd col

## modify arr elements

arr[0][0]=100
print(arr)

## statistical concept --normalization
## to have mean of 0 and std of 1
data=np.array([1,2,3,4,5])

mean=np.mean(data)
std_dev=np.std(data)

print('mean: ',mean)
print('std: ',std_dev)

normalized_data=(data-mean)/std_dev
print('Normalized data: ', normalized_data)

variance=np.var(data)  
print('Variance: ',variance)

## LOGICAL OPERATIONS

data=np.array([1,2,3,4,5,5,67,4,21,312,1])
print(data>5) # Boolean array

print(data[data>5])
print(list(filter(lambda x:x>5,data)))
ans=[]
for item in data:
    if item>5:
        ans.append(item)

print(ans)