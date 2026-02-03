

class Car:

    def __init__(self, model, year, color, for_sale):
        self.m = model
        self.y = year
        self.c = color
        self.fs = for_sale

    def __str__(self):
        return f"Car Model : {self.m}, Year : {self.y}, color : {self.c}, for_sale : {self.fs}"

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("BMW", 2025, "gray", True)
car3 = Car("Porsche", 2025, "blue", False)

# cal these objects with out __str__() result will address
print(car1)
print(car2)
print(car3)