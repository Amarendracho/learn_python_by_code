

# pass is a null statement. means: “Do nothing, but don’t cause an error.”
# EMPTY BLOCKS ARE NOT ALLOWED FOR CLASS, METHODS, BLOCKS...
# SO WE USE - pass k/w MAKE CLASS OR METHOD SHOULD NOT BE EMPTY


class PassKeyword:
    pass

    # pass constructor
    def __init__(self):
        pass

    # pass method
    def display(self):
        pass


# pass examples
# When you know structure first, logic later. know the design logic later
#“Methods exist, I’ll implement them later.”
class BankAccount:

    # pass methods
    def deposit(self):
        pass

    def withdrew(self):
        pass

    # pass block
    if True:
        pass

