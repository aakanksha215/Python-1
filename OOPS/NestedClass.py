

class Student:

    def __init__(self,name,rollno) -> None:
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self) -> None:
            self.brand = 'HP'
            self.cpu = 'i5'    
            self.ram = 8

        def show(self):
            print(self.brand)
            print(self.cpu)
            print(self.ram)



s1 = Student('Urvi',58)
s2 = Student('Avi',5)

s1.show()

lap1 = Student.Laptop()
