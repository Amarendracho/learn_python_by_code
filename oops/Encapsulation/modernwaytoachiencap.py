# advance way to achieve encapsulation
# using @property @propertymethodname.setter
# Benefits : add additional logic when you read, write, or delete attributes


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


class House:
    def __init__(self, house_number, location):
        self.__hnum = house_number
        self.__loc = location

    @property
    def house_num(self):
        return self.__hnum

    @property
    def location(self):
        return self.__loc

    @house_num.setter
    def house_num(self, house_number):
        self.__hnum = house_number

    @location.setter
    def location(self, location):
        self.__loc = location


h1 = House("1-123 C LINCON ST, USA", "VERMILLION, SD")
print(h1.house_num, h1.location)
