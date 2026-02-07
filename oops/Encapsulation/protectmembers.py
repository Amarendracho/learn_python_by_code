# Protected members are variables or methods that are intended to be
#                                                   accessed only within the class and its subclasses.

# only accessed in class and subclass. protected variables defined with a single underscore prefix.
#                                                    (_varibalename)


class Property:
    def __init__(self, name, cost):
        self.name = name
        self._property_cost = cost # protected member

    def _property_details(self):
        print(f"{self.name} and cost of the property is {self._property_cost}")

class House(Property):
    def __init__(self, name, cost, bedrooms):
        super().__init(name,cost)
        self.bed = bedrooms

    def house_property(self, bedrooms):
        print(f"{self.name} and beds {self.bed} and {self._property_cost}")

house = House("House", 150000)
house.house_property(3)