
a = 5
b = 4
c = 6
d = 8

# using temp variable 
temp = a
a  = b
b = temp
#using formula
c = c + d
d = c - d
c = c - d
#using XOR
c = c ^ d
d = c ^ d
c = c ^ d

# pythonic way
a,b = b,a

print(a)
print(b)
print(c)
print(d)