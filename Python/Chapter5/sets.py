# sets => collection of non - repetative items (all elements are unique)

s = {4, 78, 9}

e = set() # empty set

set1 = {99, 55.5, "Tini"}

print(type(set1))
set1.add(889)
print(set1)

# sets are unordered
# unindexed - can't be accessed by index
# can not change items in sets
# can not contain duplicate values

s1 = {87, 67, 44, 2}
s2 = {2, 99, 5, 23, 34}

print(s1.union(s2))
print(s2.intersection(s2))


