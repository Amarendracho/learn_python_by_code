# In a multilevel class hierarchy, super() ensures that all parent constructors are executed in the correct order,
# avoiding duplicate code and properly initializing all inherited attributes.


# Python uses Method Resolution Order (MRO) to determine the sequence in which parent classes are searched.
# When super() is used.


class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def emp_details(self):
        print(self.name, "- Is Employee")

class Manager(Employee):
    def team(self, team):
        print(self.name, "- Is manages" , team , "team")

emp1 = Manager("Amarendra")
emp1.emp_details()
emp1.team("tech")

class Phone:
    def __init__(self, model):
        print("phone model : ", model)

class Iphone(Phone):
    def __init__(self, model):
        print(model, "Model Not present in Iphone")
        super().__init__(model)

class Samsung(Iphone):
    def __init__(self, model):
        print(model, "Model Not present in Samsung")
        super().__init__(model)

class Nokia(Samsung):
    def __init__(self, model):
        print("Nokia Model : ", model)
        super().__init__(model)

phone = Nokia("Lumia 630")

