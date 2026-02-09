# Encapsulation means hiding internal details of a class and only exposing what’s necessary.
# It helps to protect important data from being changed directly and keeps the code secure and organized.

# we can achieve encapsulation in 3 ways access modifiers, getters & setters , @property


class Employee:

    def __init__(self, name , salary):
        self.name = name  # public attribute
        self.__salary = salary # private attribute

emp1 = Employee("Tanish", 79000)
print(emp1.name) # tanish
print(emp1.__salary)


# self.name = name: Public attribute, can be accessed directly.
# self.name = name: Public attribute, can be accessed directly.
# emp1.__salary not accessed - AttributeError: 'Employee' object has no attribute '__salary'