# private members and methods cannot accessed outside the class
# define using double underscore (self.__name/ def __details())


class Account:
    def __init__(self, balance):
        self.__bal = balance

    def acc_bal(self):
        return f"Account Balance : {self.__bal}"

acc = Account(12000)
#print(acc.__bal) # can not access directly
print(acc.acc_bal())





class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.__salary = salary

    def show_salary(self):
        print("salary :" , self.__salary)

emp = Employee("Mark", 150000)
print(emp.name)
#print(emp.__salary) # # Error: Not accessible directly
emp.show_salary() # right way to use private