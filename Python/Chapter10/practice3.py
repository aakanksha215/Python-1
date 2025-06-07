class Demo:
    a = 10

obj = Demo()  

print(obj.a) # class attribute because instance attribute is not present

obj.a = 0 # instants attribute is set

print(obj.a) # print instance attribute

print(Demo.a) # prints the class attribute