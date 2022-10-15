# declaration and defination of function
def greet():
    print('Hello')
    print('Good Morning')

# calling of function
greet()

# parametrised function
def sum(a,b):
    c = a + b
    print(c)

sum(2,3)    

# returinig values
def find(x,y):
    s = x+y
    d = x-y
    return s,d

result1,result2 = find(9,5)
print(result1)
print(result2)