# __init__ method in Python is a constructor.
# It runs automatically when a new object of a class is created.
# Its main purpose is to initialize the object’s attributes and set up its initial state.


#__init__ with Parameters
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Human("patric", 19)
person2 = Human("Justin", 24)

print(person1.name , person1.age)
print(person2.name , person2.age)


#Default Parameters in __init__
class OpenAiModels:

    def __init__(self, model_name, age=2, usage = "AI"):
        self.model_name = model_name
        self.age = age
        self.usage = usage

model1 = OpenAiModels("chatgpt")
model2 = OpenAiModels("gemini", 3, "google AI")

print(model1.model_name, model1.age, model1.usage)
print(model2.model_name, model2.age, model2.usage)



