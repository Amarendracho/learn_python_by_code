# Protected members are variables or methods that are intended to be
#                                                   accessed only within the class and its subclasses.

# only accessed in class and subclass. protected variables defined with a single underscore prefix.
#                                                    (_varibalename)
# Best use case in inheritance


class Account:
    def __init__(self, balance):
        self._bal = balance

class Wellsfargo(Account):

    def user_account(self):
        print(f"My wells fargo bank balance is : {self._bal}")

acc = Account(43000)
print(acc._bal) # not recommended best use case inheritance

bank1 = Wellsfargo(67000)
bank1.user_account()



#Example 2
class Property:
    def __init__(self, name, cost):
        self.name = name
        self._property_cost = cost # protected member

    def _property_details(self):
        print(f"property is : {self.name} and cost : {self._property_cost}")

class House(Property):
    def __init__(self, name, cost, bedrooms):
        super().__init__(name,cost)
        self.bed = bedrooms

    def house_property(self):
        super()._property_details()
        print(f"It has {self.bed} rooms")
        #print(f"{self.name} and beds {self.bed} and {self._property_cost}")

house = House("House", 150000, 3)
house.house_property()


class Manager:
    def __init__(self, name, age):
        self.name = name # public
        self._age = age # protected

class Employee(Manager):

    def show_details(self):
        return f"Employee age : {self._age}" # access protected variable in subclass

emp1 = Employee("Chaile", 23)
print(emp1.name)
print(emp1.show_details())


















