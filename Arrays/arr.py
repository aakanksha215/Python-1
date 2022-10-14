from array import *

vals = array('i',[2,6,-9,8,4,5])

print(vals)

print(vals.buffer_info())

newArr = array(vals.typecode,(a*a for a in vals))

print(newArr)

i=0
while i<len(newArr):
    print(newArr[i])
    i=i+2