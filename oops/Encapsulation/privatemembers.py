# private members and methods cannot accessed outside the class
# define using double underscore (self.__name/ def __details())
# private data members accessed via 2 ways - method and setters&getters()


class Account:
    def __init__(self, balance):
        self.__bal = balance

    # one way to get private attributes access
    def acc_bal(self):
        return f"Account Balance : {self.__bal}"

    # second way
    def get_bal(self):
        return self.__bal

    def set_bal(self, balance):
        if balance > 0:
            self.__bal = balance

acc = Account(12000)

#print(acc.__bal) # can not access directly
#print(acc.acc_bal())
acc.set_bal(15000)
print(acc.get_bal())




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