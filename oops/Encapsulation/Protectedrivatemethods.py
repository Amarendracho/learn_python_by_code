# protected method define - def _methodname(self)
# private method define - def __methodname(self)


class BankAccount:

    def __init__(self):
        self.balance = 10000

    def _show_balance(self): # protected method
        return f"Account balance: {self.balance}"

    def __update_balance(self, amount): # private method
        self.balance += amount

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)  # Accessing private method internally
            self._show_balance() #Accessing protected method
        else:
            print("Invalid deposit amount!")

wells = BankAccount()
print(wells._show_balance())
# print(wells.__update_balance) #Error: private method
print(wells.deposit(5000))

