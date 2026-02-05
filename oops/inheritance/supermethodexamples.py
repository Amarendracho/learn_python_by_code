# super() function is used to call methods from a parent (superclass) inside a child (subclass).
#  It allows you to extend or override inherited methods while still reusing the parent’s functionality.



# Simple super() example
class Phone:

    def __init__(self, model_name, color,is_internet):
        self.name = model_name
        self.color = color
        self.is_internet = is_internet

    def phone_properties(self):
        return (f"Phone Model : {self.name}\n"
                f"Phone color : {self.color}\n"
                f"Phone have Internet connection : {self.is_internet}")

class Iphone(Phone):
    def __init__(self, model_name, color,is_internet,camara):
        super().__init__(model_name, color, is_internet)
        self.camara= camara

    def iphone_properties(self):
        iphone_feature = super().phone_properties()
        return (f"{iphone_feature}\n"
                f"camara pixels : {self.camara}")

iphone1 = Iphone("IPHONE-17-PROMAX", "Silver", True, "50MP")
print(iphone1.iphone_properties())



# Intermediate super() example include method super() and constructor super()
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


