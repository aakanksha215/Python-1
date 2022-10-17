
# instance method -- > 
# (
# 1. Accessor Method --> (get method)
# 2. Mutator Method --> (set method)
# )

# class method -- > (access class methods)
# static method

class Student:
    school = 'MySchool'
    def __init__(self,m1,m2,m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3    

    @classmethod    
    def getschool(cls):
        return cls.school

    @staticmethod    
    def info():
        print("This is Student class ")    


s1 = Student(36,78,98)
s2 = Student(54,67,89)

print(s1.avg())
print(s2.avg())

print(Student.getschool())
print(Student.info())