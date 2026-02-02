class Student:

    def __init__(self, name, grade):
        self.name = name
        self.age = grade

    @classmethod
    def student_info(cls):
        return f"{cls.name} = {cls.grade}"

student1 = Student("Amar", 3.9)
student2 = Student("jenny", 4.0)
print(student1.student_info())