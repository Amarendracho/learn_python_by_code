# class variables = shared among all instances(objects) of a class.
#                    class variables defined outside the constructors.
#                    calling class variables by obj reference and class_name.variable_name(recommended)



class House:
    walls = True
    bedrooms= 3

obj1 = House()
obj2 = House()

print(obj1.bedrooms, obj1.walls)
print(House.bedrooms, House.walls)


# with instance variables
class Student:

    university_name = "Stanford"
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("James", 25)
student2 = Student("Jim", 30)

# change the class variable value
Student.university_name = "Harvard"

# calling with object name and class name
print(student1.name, student1.age, student1.university_name, "or" , Student.university_name)
print(Student.num_students)
