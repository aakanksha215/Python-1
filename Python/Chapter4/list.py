friends = ["Apple", "Grapes", 98 , True , 83.76 , "Tini" , "Mummy"]

print(friends[3])

#   Lists are mutable

friends[2] = 74
print(friends[2])

print(friends[1 : 4])

# append function---->
friends.append("shrey")
print(friends)

l1 = [2,56,78,23,55,91,28]
l1.insert(3,7000) # insert 7000 at index 3
l1.sort()
l1.reverse()
l1.pop(3)

print(l1) 