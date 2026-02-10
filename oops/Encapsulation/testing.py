

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, balance):
        if balance > 0:
            self.__balance += balance
            return self.__balance
        else:
            return "Invalid Balance"

amex = BankAccount(1000)
amex.deposit(500)
print(amex.get_balance())