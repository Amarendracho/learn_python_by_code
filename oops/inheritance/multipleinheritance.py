
# In multiple inheritance, a child class can inherit from more than one parent class.


# multilevel inheritance with different methods
class A:
    def method_a(self):
        print("A - CLASS METHOD")

class B:
    def method_b(self):
        print("B - CLASS METHOD")

class C(A,B):
    pass

obj = C() # C inherit both A,B
obj.method_a()
obj.method_b()


# multilevel inheritance with same methods - python follow MRO(Model Resolution Order)
# MRO check LEFT - TO - RIGHT (priority)

class House:

    def bedroom_count(self):
        print("House have 3 bedroom")

class Flat:

    def bedroom_count(self):
        print("Flat have 2 bedroom")

class Villa(Flat,House):
    pass

obj = Villa()
obj.bedroom_count()

