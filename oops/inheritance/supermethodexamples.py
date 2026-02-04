# super() function is used to call methods from a parent (superclass) inside a child (subclass).
#  It allows you to extend or override inherited methods while still reusing the parent’s functionality.


class Flight:
    def __init__(self, flight_number, business_cls_status, destination):
        self.fnumber = flight_number
        self.busi_c_st = business_cls_status
        self.dest = destination

    def flight_details(self):
        return (f"Flight number : {self.fnumber} \nIs business class present : {self.busi_c_st} \n"
                f"Flight destination : {self.dest}")

class Qatar(Flight):

    def __init__(self, flight_number, business_cls_status, destination, entertainment):
        super().__init__(flight_number, business_cls_status, destination)
        self.entertainment = entertainment

    def welcome(self):
        return f"Welcome to Qatar Airways 🛫"

   #override method
    def flight_details(self):
        details = super().flight_details()
        return details + f"\nIn-flight entertainment available : {self.entertainment}"



class AirIndia(Qatar):
    def __init__(self, flight_number, business_cls_status, destination, entertainment, food):
        super().__init__(flight_number, business_cls_status, destination,entertainment)
        self.food = food

    def welcome(self):
        return f"Welcome to Air India 🇮🇳"

    # override method
    def flight_details(self):

        details = super().flight_details()
        return details + f"\nIn-flight food available : {self.food}"

qatar = Qatar("QA564",True, "Dubai", True)
air= AirIndia("AI7877", False, "Delhi", True, True)
print(air.welcome())
print(air.flight_details())


