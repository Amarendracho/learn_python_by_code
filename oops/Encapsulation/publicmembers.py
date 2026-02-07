# public members(variables), and public methods can accessed from anywhere inside the class,
#                                                                       outside the class or from other modules.
# By default, all members in Python are public. They are defined without any underscore prefix


class Phone:
    def __init__(self, model, cost):
        self.model = model  # public members/attributes
        self.cost = cost

    def mobile_details(self):  # public method
        print(self.model, "cost is ", self.cost)

iphone = Phone("IPHONE 17 PRO MAX", 1200)
samsung = Phone("SAMSUNG S25 ULTRA", 1450)

iphone.mobile_details() # accessed
samsung.mobile_details() # accessed