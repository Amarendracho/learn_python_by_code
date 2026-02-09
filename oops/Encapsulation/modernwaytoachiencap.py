# advance way to achieve encapsulation
# using @property @variable_name.setter


class Account:
    def __init___(self, balance):
        self.__bal = balance # private variable

    @property
    def balance(self):
        return self.__bal

    @balance.setter
    def balance(self, balance):
        if balance > 0:
            self.__bal = balance

city = Account()
city.balance(25000)
print(city.balance)
