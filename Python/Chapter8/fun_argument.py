def printMyName(name):
    print(name)


printMyName("Tini")


### function with parameters
def fun(name, str):
    print(name)
    print(str)
    return "Hello"

Get = fun("Tini", "Thank you")
print(Get)    



### function with default value
def fun2(name, str="Thank you"):
    print(f"Hello {name}")
    print(str)


fun2() 