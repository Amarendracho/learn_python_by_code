class Car:

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def start(self):
        return f"{self.model} is started"

    def stop(self):
        return f"{self.model} is stopped"

class Mustang(Car):

    def __init__(self, model, color, wheels, sports_engine):
        super().__init__(model,color)
        self.sports_engine = sports_engine

    def engine(self):
        return f"{self.model} have sports engine {self.sports_engine}"

class Bmw(Mustang):

    def performance(self):
        return f"{self.model} has Better performance"


mustang_gt = Mustang("MustangGT", "Red", 4, "5.0 V8 Engine")
bmw5 = Bmw("BMW5","light-blue", 4,"3 L V3 Engine")

print(mustang_gt.model, mustang_gt.color)
print(mustang_gt.engine())
print(bmw5.model, bmw5.color)
print(bmw5.performance())