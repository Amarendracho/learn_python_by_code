# multiple child classes inherits same parent class


class Parents:
    def __init__(self, money):
        self.money = money

class Son(Parents):
    def travel(self):
        return f"with parents money - {self.money} want travel"

class Daughter(Parents):
    def study(self):
        return f"with parents money - {self.money} want study"

son1 = Son("henry")
print(son1.travel())

daughter1 = Daughter("Nancy")
print(daughter1.study())