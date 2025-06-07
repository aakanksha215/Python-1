# Object Oriented Programming

class Employee:
    name = "Shrey"
    language = "Java"
    salary = 1500000

    def __init__(self):
        print("Im creating an object")
        self.name = name
        self.language = language
        self.salary = salary
    

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good Morning")    

    @staticmethod
    def welcome():
        print("Welcome to company")


# creating object

shrey = Employee()
language = "Python"

# Instance attributes get preference over Class attributes

print(shrey.language, shrey.salary)    