# private members and methods cannot accessed outside the class
# define using double underscore (self.__name/ def __details())


class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.__salary = salary

    def show_salary(self):
        print("salary :" , self.__salary)

emp = Employee("Mark", 150000)
print(emp.name)
print(emp.__salary) # # Error: Not accessible directly
emp.show_salary() # right way to use private