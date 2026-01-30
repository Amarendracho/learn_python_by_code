class test:

    def __init__(self, name, age):
        self.name = name
        self.age= age

    def details(self):
        print(self.name , self.age)

obj = test("Amar",29)

obj.details() 