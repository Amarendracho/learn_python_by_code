

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
obj1.display() # Display nothing because it pass the blocks
