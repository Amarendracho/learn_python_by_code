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