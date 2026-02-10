# protected method define - def _methodname(self)
# private method define - def __methodname(self)


class BankAccount:

    def __init__(self):
        self.balance = 10000

    def _show_balance(self): # protected method
        return f"Account balance: {self.balance}"

    def __update_balance(self, amount): # private method
        update_bal = self.balance - amount
        return f"withdrew amount {amount} \nAvailable balance: {update_bal}"

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)
            self._show_balance()
        else:
            print("Invalid deposit amount!")

wells = BankAccount()
print(wells._show_balance())

