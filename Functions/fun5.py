# Global variable in python

a = 10
b = 12
print(id(a))

# inside a function preference is given to local variable

def fun():
    global a # to chang global variable

    # globals will give all the global variable

    x = globals()['a']
    print(id(x))
    a = 12
    print(a)



fun()
print(a)    