# object is instance of class
# It holds its own set of data (instance variables) and can invoke methods defined by its class.
# when you create object of class default __init__() calls automatically (internally)


class Student:

    student_university = "MIT"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_details(self):

        #calling instance variables and also class variables inside instance method
        return f"student name : {self.name}, age : {self.age} from {Student.student_university}"

# creating 3 student objects
student1 = Student("Harry", 25)
student2 = Student("Jenny", 23)
student3 = Student("Mark", 26)

print(student1.student_details()) # calling instance method using object reference
print(student2.student_details())
print(student3.student_details())

# print(student1.student_details())
# print(student1.student_university)
# print(Student.student_university)

