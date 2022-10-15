
# decorator can change the behaviour of existing functions

#A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

def div(a,b):
    print(a/b)


def smart_div(fun):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return fun(a,b)

    return inner


div = smart_div(div)

div(2,4)
