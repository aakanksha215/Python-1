class Employee:
    company = "Adobe"
    def show(self):
        print(f"The name is {self.name} an the salary is {self.salary}")


class Programmer(Employee):
    def showLanguage(self):
        print("Language")

        
