class Car:

    def __init__(self, model, year, color, for_sale):
        self.m = model
        self.y = year
        self.c = color
        self.fs = for_sale

    def __str__(self):
        return f"Car Model : {self.m}, Year : {self.y}, color : {self.c}, for_sale : {self.fs}"