
# can not create object of abstract class
# abstract class must have one abstract method


from abc import ABC,abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("Running")



lap = Laptop()

lap.process()