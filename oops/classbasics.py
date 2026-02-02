
""" A CLASS IS COLLECTION OF STATE(variables) and BEHAVIOR(methods)
    TO CREATE A CLASS KEYWORD IS class classname,
   THIS IS CLASS WITH CLASS VARIABLE
   FETCHING CLASS VARIABLE USING CLASSNAME.VARIABLE NAME
   CLASS HAVE CLASS VARIABLES INSTANCE VARIABLES (variables inside constructor) __init__ method"""

class Employee:
    name = "Amarendra"

print(Employee.name)


# Example
class Human:

    gender = "Male"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name : {self.name}, Age : {self.age}")

amar = Human("Amarendra", 29)
tanish = Human("Tanish", 6)

amar.details()
tanish.details()