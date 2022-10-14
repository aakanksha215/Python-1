from numpy import *

arr = array([2,5,6,7,8,9])

# add 10 to each eement 
arr = arr + 10
print(arr)

# adding 2 arrays
arr2 = array([1,1,3,6,7,5])
arr = arr + arr2
print(arr)

# array copy
a = array([1,2,3,4,5,6])
b = a
print(a)
print(b)

c = a.view()
print(c)
print(id(c))
print(id(a))

d = a.copy()
print(d)
print(id(a))
print(id(d))