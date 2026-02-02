# __init__ method in Python is a constructor.
# It runs automatically when a new object of a class is created.
# Its main purpose is to initialize the object’s attributes and set up its initial state.


#__init__ with Parameters
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# person1 = Human("patric", 19)
# person2 = Human("Justin", 24)
#
# print(person1.name , person1.age)
# print(person2.name , person2.age)


#Default Parameters in __init__
class OpenAiModels:

    def __init__(self, model_name, usage = "AI" , age=2):
        self.model_name = model_name
        self.usage = usage
        self.age = age


model1 = OpenAiModels("chatgpt", "openai")
model2 = OpenAiModels("gemini", "google AI", 3 )
model3 = OpenAiModels("claude", "claude ai",1, )
model4 = OpenAiModels("grook","twitter")

print(model1.model_name, model1.age, model1.usage)
print(model2.model_name, model2.age, model2.usage)
print(f"{model3.model_name}, age-{model3.age}, owned by-{model3.usage}")
print(model4.model_name, model4.age, model4.usage)



