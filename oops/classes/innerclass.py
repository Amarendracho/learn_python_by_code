"""In Python: An inner class is a class defined inside a class.
                They are just normal classes
                Defined inside another class
                Mainly used for logical grouping
            Inner class objects depending on outer class, We can create inner class obj with help of outer class"""


# Example University - Department
class University:
    def __init__(self,universityName):
        self.universityName = universityName

    class Department:
        def __init__(self, deptName, staff):
            self.deptName = deptName
            self.staff = staff

        def department_info(self):
            print(f"Department is: {self.deptName}\n"
                  f"No of Staff: {self.staff}")

 # outer class object creation
university1 = University("UNIVERSITY OF PITTSBURGH")
print(university1.universityName)
# Create an Inner class obj with the help of outer class
department1 = University.Department("Checimal Department", 15)
department1.department_info()


# fetching outer class attributes inside inner class
        # inner classes are not child classes
        # Inner classes are (NO INHERITANCE)

class University:
    def __init__(self, name):
        self.name = name
    class Department:

        def __init__(self,outer ,name, staff):
            self.outer = outer
            self.name = name
            self.staff = staff

        def dept_info(self):
            # outer.outclassattributename
            print(f"University Name: {self.outer.name}\n" 
                  f"Department Name: {self.name}\n"
                  f"Staff: {self.staff}")

uni1 = University("MIT")
computer_dept = University.Department(uni1, "Computer Science", 25)
computer_dept.dept_info()

class Iphone:
    def __init__(self, name):
        self.name = name

    class ModelName:
        def __init__(self,outer, name, cost):
            self.outer = outer
            self.name = name
            self.cost = cost

        def mode_info(self):
            print(f"{self.outer.name}\n"
                  f"{self.name}\n"
                  f"${self.cost}")

phone1 = Iphone("IPHONE 18 SERIES")
model1 = Iphone.ModelName(phone1, "IPHONE - 18", 629.00)
model2 = Iphone.ModelName(phone1, "IPHONE - 18 PLUS", 750.00)
model3 = Iphone.ModelName(phone1, "IPHONE - 18 PRO", 1099.00)
model4 = Iphone.ModelName(phone1, "IPHONE - 18 PRO MAX", 1299.00)

model1.mode_info()
model2.mode_info()
model3.mode_info()
model4.mode_info()
