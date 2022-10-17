
# instance variable are inside __init__ function
# class variable (static variables) are outside __init__ function

class Car:

    wheels = 4
    def __init__(self):
        self.mil = 20
        self.comp = "BMW"


c1 = Car()
c2 = Car()

c2.mil = 40

Car.wheels = 6

print(c1.comp, c1.mil,c1.wheels)
print(c2.comp, c2.mil,c2.wheels)