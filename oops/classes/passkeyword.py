

# pass is a null statement. means: “Do nothing, but don’t cause an error.”
# EMPTY BLOCKS ARE NOT ALLOWED FOR CLASS, METHODS, BLOCKS...
# SO WE USE - pass k/w MAKE CLASS OR METHOD SHOULD NOT BE EMPTY


class PassKeyword:
    pass

    def __init__(self):
        pass

    def display(self):
        pass

obj1 = PassKeyword()
obj1.display() # Display nothing because it passes the blocks


# pass examples
# When you know structure first, logic later. know the design logic later

class BankAccount:

    def deposit(self):
        pass

    def withdrew(self):
        pass

#“Methods exist, I’ll implement them later.”