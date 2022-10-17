# Inheritance in python
# super keyword
# Method resolution Object (MRO)
# To represent the super class we use super method

class A:
    def __init__(self) -> None:
        print("In A init")

    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")    


class B:
    def __init__(self) -> None:
        print("In A init")

    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")    


class C(A,B):
    def __init__(self) -> None:
        super().__init__()
        print("In C init")

    def feature5(self):
        print("This is feature 5")

    def feature6(self):
        print("This is feature 6")    



a1 = A()

a1.feature1()
a1.feature2()

b1 = B()



c1 = C()
