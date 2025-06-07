# string in python is immutable
# string is a datatype

# slicing of string --->

name ="aakanksha"

nameslice = name[0 : 4] # start from index 0 all the way till 4 (excluding 4)
print(nameslice)

# negative slicing ---->

name1 = "Piyush"
print(name1[-3 : -1])

print(name1[4:])
print(name1[:1])

# slicing with skip values --->

print(name1[1 : 4 : 2])