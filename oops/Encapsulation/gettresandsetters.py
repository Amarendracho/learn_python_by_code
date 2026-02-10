
# second approach to achieve encapsulation using getters and setters methods.
# set_balance - set the balance
# get_balance - get the balance
# using getters and setters we cannot achieve 100% Encapsulation. because we can modify setter() method.

class Bank:
    def __init__(self):
        self.__num_customers = 1000

    # get method
    def get_NumberOfCustomers(self):
        print("Initial customers:", self.__num_customers)

    #set method
    def set_NumberOfCustomers(self, num_customers):
        if num_customers > 0:
            self.__num_customers += num_customers
            print("After updating Total customers:", self.__num_customers)
        else:
            print("Invalid Customer Number:",num_customers)

    # achieve 100 encap
    def total_Customers(self, number):
        self.get_NumberOfCustomers()
        self.set_NumberOfCustomers(number)

# city = Bank()
# print(city.get_NumberOfCustomers())
# city.set_NumberOfCustomers(4000)
# print(city.get_NumberOfCustomers())

# actual Encap
wells = Bank()
wells.total_Customers(4000)