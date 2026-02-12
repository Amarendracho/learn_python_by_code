# A class method works with the class itself. (not individual objects)
# uses - (cls) keyword. Depends on the class
# Define static method use - @classmethod  Decorator

# class Student:
#
#     student_count = 0 # class variable
#     total_gpa = 0
#
#     def __init__(self, name, gpa):
#         self.name = name
#         #update class attribute
#         Student.student_count += 1
#         Student.total_gpa += gpa
#
#     @classmethod
#     def student_total_count(cls):
#         print(f"Student count: {cls.student_count}")
#
#     @classmethod
#     def avg_gpa(cls):
#         if cls.student_count == 0:
#             return 0
#         else:
#             return f"Student average GPA: {cls.total_gpa / cls.student_count}"
#
# stu1 = Student("Mario", 3.3)
# stu2 = Student("Ben10", 4.0)
# stu3 = Student("Pokiman", 3.8)
# stu4 = Student("Mindcraft", 2.0)
# Student.student_total_count()
# print(Student.avg_gpa())


