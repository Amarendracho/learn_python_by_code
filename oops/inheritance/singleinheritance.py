#In single inheritance, a child class inherits from just one parent class.

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Employee inherits from Person
    def show_role(self):
        print(self.name, "is an employee")

emp = Employee("Michel")
print("Name:", emp.name)
emp.show_role()