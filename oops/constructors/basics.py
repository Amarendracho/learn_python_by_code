# A constructor in Python is a special method __init__() that is automatically executed when an object is created.
# The constructor is defined using the __init__(self, ...) method.
# A constructor is typically used to initialize instance variables.
# Default values can be provided as default parameters in the constructor.
# Instance variables store data that belongs to a specific object.
# Default parameter values allow a constructor to assign values automatically if no arguments are provided during object creation.
# python supports 1 constructor inside a class. python not supports constructor overloading like java.
# Because Python does not support method overloading by signature.

#constructor with instance variables
class Table:

    # 1 Approach default values initialization inside a constructor
    # def __init__(self):
    #     self.height = 10
    #     self.width = 20
    #
    # def default_measurements(self):
    #     return f"{self.height}cm {self.width}cm"

    # 2 Approach default values initialization when constructor init
    # def __init__(self, height = 5, width = 10):
    #     self.height = height
    #     self.width = width

    # 3 Approach variable value initialization happen when object creation
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # def __new__(cls):
    #     print("calls first")
    #     return super().__new__(cls)

#table = Table()

table = Table(10,20)
# print(table.height)
# print(table.width)
# print(table.default_measurements())

# print(table.height)
# print(table.width)

# print(table.height)
# print(table.width)