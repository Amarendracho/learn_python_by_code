# advance way to achieve encapsulation
# using @property @variable_name.setter

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property # act as getter
    def salary(self):
        return self.__salary

    @salary.setter # act as setter
    def salary(self, amount):
        if amount > 0:
            self.__salary = amount

e = Employee(50000)
print(e.salary)    # looks like variable
e.salary = 60000   # but validated
print(e.salary)
