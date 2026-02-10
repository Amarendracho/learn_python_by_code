# Just checking the actual poly works are not

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    # def set_balance(self, balance):
    #     self.__balance = balance

    def deposit(self, balance):
        if balance > 0:
            self.__balance += balance
            return self.__balance
        else:
            return "Invalid Balance"

# This is not actual poly because we are able to change the set_balance(which is incorrect)
# bank1 = BankAccount(1000)
# print(bank1.get_balance())
# bank1.set_balance(1500)
# print(bank1.get_balance())

amex = BankAccount(1000)
amex.deposit(500)
print(amex.get_balance())