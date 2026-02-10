# protected method define - def _methodname(self)
# private method define - def __methodname(self)


class BankAccount:
    def __init__(self):
        self.balance = 1000

    # Protected method
    def _show_balance(self):
        print(f"Inital Balance: ${self.balance}")

    # Private method
    def __update_balance(self, amount):
        self.balance += amount
        print(f"Update Balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self._show_balance()  # Accessing protected method
            self.__update_balance(amount)  # Accessing private method internally
        else:
            print("Invalid deposit amount!")


account = BankAccount()
#account._show_balance()  # Works, but should be treated as internal
# account.__update_balance(500)  # Error: private method
account.deposit(500)  # Uses both methods internally

