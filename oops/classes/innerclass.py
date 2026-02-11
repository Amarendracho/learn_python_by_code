"""In Python: An inner class is a class defined inside a class.
                They are just normal classes
                Defined inside another class
                Mainly used for logical grouping
            Inner class objects depending on outer class, We can create inner class obj with help of outer class"""


# Example University - Department
# class University:
#     def __init__(self,universityName):
#         self.universityName = universityName
#
#     class Department:
#         def __init__(self, deptName, staff):
#             self.deptName = deptName
#             self.staff = staff
#
#         def department_info(self):
#             print(f"Department is: {self.deptName}\n"
#                   f"No of Staff: {self.staff}")
#
#  # outer class object creation
# university1 = University("UNIVERSITY OF PITTSBURGH")
# print(university1.universityName)
# # Create an Inner class obj with the help of outer class
# department1 = University.Department("Checimal Department", 15)
# # fetching inner class attributes
# print(department1.deptName) # Checimal Department
# department1.department_info()
#
#
# # fetching outer class attributes inside inner class
#         # inner classes are not child classes
#         # Inner classes are (NO INHERITANCE)
#
# class University:
#     def __init__(self, uni_name):
#         self.uni_name = uni_name
#
#     class Department:
#         def __init__(self,outer ,name, staff):
#             self.outer = outer  # store outer object
#             self.name = name
#             self.staff = staff
#
#         def dept_info(self):
#             # outer.outclassattributename
#             print(f"University Name: {self.outer.uni_name}\n"
#                   f"Department Name: {self.name}\n"
#                   f"Staff: {self.staff}")
#
# uni1 = University("MIT")
# computer_dept = University.Department(uni1, "Computer Science", 25)
# computer_dept.dept_info()
#
# #fetching inner class attributes
# print(computer_dept.name)
# print(computer_dept.staff)
#
#
# # Example 3
# class Iphone:
#     def __init__(self, name):
#         self.name = name
#
#     class ModelName:
#         def __init__(self,outer, name, cost):
#             self.outer = outer # store outer object
#             self.name = name
#             self.cost = cost
#
#         def mode_info(self):
#             print(f"{self.outer.name}: Model: {self.name}, Cost: ${self.cost}")
#
# phone1 = Iphone("IPHONE 18 SERIES")
# model1 = Iphone.ModelName(phone1, "IPHONE - 18", 629)
# model2 = Iphone.ModelName(phone1, "IPHONE - 18 PLUS", 750)
# model3 = Iphone.ModelName(phone1, "IPHONE - 18 PRO", 1099)
# model4 = Iphone.ModelName(phone1, "IPHONE - 18 PRO MAX", 1299)
#
# model1.mode_info()
# model2.mode_info()
# model3.mode_info()
# model4.mode_info()


# example 4 moderate
class Company:

    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company = Company("Google")
company.add_employee("Sundar", "CEO")
company.add_employee("Amarendra", "Software Engineer")
company.add_employee("Jenny", "Security Engineer")

print(company.list_employees())

# using iteration
for employee in company.list_employees():
    print(employee)






