# in python integer,strings are immutable so new memory is allocated
def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print(x)


a = 10
print(id(a))
update(a)    
print(a)

# in python list is mutable so new memory is not allocated

def change(l):
    print(id(l))
    l[1] = 15
    print(id(l))
    print(l)

lst = [12,16,18]
print(id(lst))
change(lst) 
print(lst)   