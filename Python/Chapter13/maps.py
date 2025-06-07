from functools import reduce 
l = [1, 4, 6, 8, 2]

square = lambda x : x*x

sqList = map(square, l)
print(list(sqList))

# Filter Example

def even(n):
    if(n%2 == 0):
        return True
    return False


onlyEven = filter(even, l)        
print(list(onlyEven))

# Reduce Example
def sum(a, b):
    return a + b

print(reduce(sum, l))    