# protected method define - def _methodname(self)
# private method define - def __methodname(self)


class BankAccount:

    def __init__(self):
        self.balance = 10000

    def _show_balance(self):
        return f"Account balance: {self.balance}"


    def __withdrew_balance(self):
        pass
