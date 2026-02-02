class Student:

    count = 0

    def __init__(self, name, grade):
        self.name = name
        self.age = grade
        Student.count +=1

    @classmethod
    def student_info(cls):
        return f"Student count = {Student.count}"

student1 = Student("Amar", 3.9)
student2 = Student("jenny", 4.0)



print(Student.student_info())