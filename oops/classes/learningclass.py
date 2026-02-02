# class can have instance & class variables
    # class can have instance, static & class methods

class University:

    # class variable accessed across the class
    university_name = "Harvard University"
    student_count = 0

    #Instance method or constructor
    def __init__(self, uni_code, location, count):
        # instance variable
        self.uni_code = uni_code
        self.location = location
        self.count= count
        University.student_count += 1

    @classmethod
    def university_details(cls):
        return f"{cls.university_name}"

    @staticmethod
    def student_details():
        print("static method")


student1 = University(101,"usa",1)
print(student1.uni_code)
print(student1.location)
print(student1.student_count)

print(University.university_details())
