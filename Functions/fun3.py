# types of arguments in python
# default
# keyword
# position
# variable length
def person(name,age = 18):
    print(name)
    print(age-5)


person(age = 15,name = 'anvi')    

# default
person('navi')

# variable length arguments
# here *b means multiple values
def sum(a,*b):
    print(a)
    print(b)
    c = a
    for i in b:
        c = c+i
    print(c)

sum(5,6,7)    