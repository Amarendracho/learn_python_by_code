# composition Strong HAS-A relationship
# Child object cannot exist without parent. Child object is owned by parent
#                                           If parent dies → child dies


class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine("4500cc") # create object inside

car = Car("Mustang")
print(car.model, car.engine.power)

# Engine is created inside Car
# Engine cannot exist without Car
# Strong ownership
