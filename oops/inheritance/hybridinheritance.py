# combination of two inheritances

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name):
        super().__init__(name)

    def role(self):
        print(self.name, "is an employee")

class Project:
    def __init__(self, projectname):
        self.projectname = projectname

class Manager(Employee, Project): # Multiple inheritance
    def __init__(self, name, projectname):
        Employee.__init__(self, name)
        Project.__init__(self, projectname)

    def details(self):
        print(self.name, "lead project" , self.projectname)

manager = Manager("Justin", "AI-MODEL DEVELOPMENT")
manager.role()
manager.details()
