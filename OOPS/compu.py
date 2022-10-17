# classes and objects in python
# __init__ method (Similar to constructor)

class Computer:

    def __init__(self,cpu,ram):
        print('In init')
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Config is '+ self.cpu, self.ram)



comp1 = Computer('i5',16)
print(type(comp1))

#Computer.config(comp1)

comp1.config()