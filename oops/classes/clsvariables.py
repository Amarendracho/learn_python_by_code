# class variables = shared among all instances(objects) of a class.
#                    class variables defined outside the constructors.
#                    calling class variables by obj reference and class_name.variable_name(recommended)


class Student:

    university_name = "Stanford"

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("James", 25)
student2 = Student("Jim", 30)

print(student1.name, student1.age, Student.university_name)