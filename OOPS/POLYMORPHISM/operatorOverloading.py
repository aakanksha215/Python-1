
# OPERATOR OVERLOADING


a = 24
b = 12

print(int.__add__(a,b))

c = '6'
d = '8'

print(str.__add__(c,d))


class Student:
    
    def __init__(self,m1,m2) -> None:
        self.m1 = m1
        self.m2 = m2


    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self) -> str:
        return '{} {}'.format(self.m1, self.m2)            



s1 = Student(58,96)
s2 = Student(34,56)

s3 = s1 + s2
print(s3.m1)

# by default it will call __str__ function

print(s1)
print(s2)