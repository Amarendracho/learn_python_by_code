# Aggregation is Weak HAS-A relationship
# Objects can exist independently, One object uses another object
#                                  Both can live independently


class Project:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self,emp_name, project):
        self.emp_name = emp_name
        self.project = project

project = Project("AI-ENGINEER")
emp = Employee("Amarendra", project)
print(emp.emp_name)
print(emp.project)
