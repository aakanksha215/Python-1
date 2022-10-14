from array import *

arr = array('i',[])

n = int(input('Enter the length of array'))

for i in range(n):
    x = int(input('Enter the next value of array'))
    arr.append(x)

print(arr)    

#find index of any number

val = int(input('Enter the value for search'))

j=0
for ele in arr:
    if ele == val:
        print(j)
        break
    j=j+1


# by using function

print(arr.index(val))    