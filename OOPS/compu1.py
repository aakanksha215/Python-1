# objects get memory in heap in python

class Computer:
    
    def __init__(self) -> None:
        self.name = 'Urvi'
        self.age = 22

    def update(self):
        self.age = 24    

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

      

c1 = Computer()
c2 = Computer()


if c1.compare(c2):
    print("Equal")


print(id(c1))

print(c1.name)
print(c2.name)
