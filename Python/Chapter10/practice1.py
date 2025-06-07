class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Rohan", 1200000, 243873)
print(p.name, p.salary, p.pin)        