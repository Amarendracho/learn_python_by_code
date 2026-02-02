# __str__() Method
#__str__ method in Python allows us to define a custom string representation of an object.
# By default, when we print an object or convert it to a string using str(), Python uses the default implementation,

class Amazon:

    def __init__(self, order_number, item_name):
        self.order_number = order_number
        self.item_name = item_name

    def __str__(self):
        return f"{self.order_number} and {self.item_name}"

obj1 = Amazon(101, "Book")
obj2 = Amazon(710, "Iphone-17")
obj3 = Amazon(410, "Chair")

print(obj1)
print(obj2)
print(obj3)