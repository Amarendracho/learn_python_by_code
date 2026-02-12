# Constructor in python special method. it automatically calls when the object is created.
# constructor define =  __init__(self)
# A constructor can contain [instance variables , default variables]
# Instance variables used for object reference and object variable implementation.
# Default variables calls with default values while we are not declare any values to instance variables
# python supports 1 constructor inside a class. python not supports constructor overloading like java.
# Because Python does not support method overloading by signature.

#constructor with instance variables
class Table:

    # 1 approach default values initialization inside a constructor
    # def __init__(self):
    #     self.height = 10
    #     self.width = 20
    #
    # def default_measurements(self):
    #     return f"{self.height}cm {self.width}cm"

    # 2 approach default values initialization when constructor init
    # def __init__(self, height = 5, width = 10):
    #     self.height = height
    #     self.width = width

table = Table()
# print(table.height)
# print(table.width)
# print(table.default_measurements())

# print(table.height)
# print(table.width)