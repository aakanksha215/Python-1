# Important python functions :---
# 1. filter() -- > takes a sequence and return a sequence
# 2. map() -- > 
# 3. reduce()


from functools import reduce

nums = [2,3,4,5,6,7,8,9]

evens = list(filter(lambda n : n%2==0 ,nums))

doubles = list(map(lambda n : n*2 ,evens))

sum = reduce(lambda a,b : a+b ,doubles)

print(evens)
print(doubles)
print(sum)