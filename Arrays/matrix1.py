from numpy import *

arr1 = array([
    [1,2,3,5,7,9],
    [4,5,6,1,9,8]
])

print(arr1)

print(arr1.dtype)
print(arr1.ndim)#give number of dimensions
print(arr1.shape)#give a tuple with number of rows and column
print(arr1.size)

#convert multidimension in 1-D array
arr2 = arr1.flatten()
print(arr2)

#convert 1-D to multi-D array
arr3 = arr2.reshape(3,4)
print(arr3)

arr4 = arr2.reshape(2,3,2)#number of array,number of rows,number of columns
print(arr4)


#convert 2-D array int o Matrix

m = matrix(arr1)
print(m)

# another way to create a matrix is 
m1 = matrix('2,4,3 ; 7,8,9 ; 5,4,6')
print(m1)
m2 = matrix('4,8,9 ; 3,2,1 ; 10,6,7')
print(m2)

# Multiply two matrix in python

m3 = m1 * m2
print(m3)


