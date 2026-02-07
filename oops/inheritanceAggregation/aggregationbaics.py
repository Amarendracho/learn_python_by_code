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

project = Project("AI-ENGINEER") # single project object
emp1 = Employee("Amarendra", project)
emp2 = Employee("Martin", project)

print(emp1.emp_name, "works on", emp1.project.name)
print(emp2.emp_name, "works on", emp2.project.name)

# One project
# Multiple employees
# Project lives independently