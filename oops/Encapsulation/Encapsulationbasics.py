# Encapsulation means hiding internal details of a class and only exposing what’s necessary.
# It helps to protect important data from being changed directly and keeps the code secure and organized.


class Employee:

    def __init__(self, name , salary):
        self.name = name  # public attribute
        self.__salary = salary # private attribute

emp1 = Employee("Tanish", 79000)
print(emp1.name, emp1.__salary)


# self.name = name: Public attribute, can be accessed directly.
# self.name = name: Public attribute, can be accessed directly.
# emp1.__salary not accessed - AttributeError: 'Employee' object has no attribute '__salary'