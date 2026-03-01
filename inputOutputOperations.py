# input and output operations is fundamental to Python programming.
#       With the print() function, we can display output in various formats,
#       while the input() function enables interaction with users by gathering input during program execution.


# Taking input in Python - input() function
# input() method return a string what to convert concat with other datatypes(int, float,...)
# print() prints the output

# name = input("Enter your favourite singer: ")
# print(name,"is My favourite singer 🎶")

# The code prompts the user to input their name, stores it in the variable "name"
# and then prints a greeting message addressing the user by their entered name.

# Printing Output using print() in Python
# This function allows us to display text, variables and expressions on the console.
#
# print("Something")

# Printing Variables

print("Person Details")
name = "MarkSloan"
age = 26
address = "1-12 BEVERLY HILLS FLORIDA"
print("Name:",name, ":)age:",age, "!address:",address)

#Take Multiple Input in Python
# We are taking multiple input from the user in a single line, splitting the values entered by the user
# into separate variables for each value using the split() method.

thing1 , thing2 = input("Enter your favourite things: ?").split()
print("My favourite thing 1: ", thing1)
print("My favourite thing 2: ", thing2)

a,b,c = input("Your Top Schools: ? ").split()
print("My Top college is:",a)
print("My second Top college is:",b)
print("My third Top college is:",c)

"""
    Note: The split() method always returns input values as strings.
    If you need them as numbers (int or float), you must convert them using typecasting.
"""

# Change the Type of Input in Python
""" By default input() function helps in taking user input as string. If any user wants
    to take input as int or float, we just need to typecast it. """

something = input("Type Any thing: ")
print(something)

# Print Numbers in Python

age = int(input("Enter age: "))
print(age)

# Print Float or Decimal Number in Python

salary = float(input("Salary : "))
print(salary)

# Find DataType of Input in Python

name = "Justin"
age = 25
salary = 123323.12
fav_food = ["Biryani", "Chicken", "Tea"]
fav_cars = ("Mustang", "Porsche", "Audi")
fav_places = {"USA": "NEWYORK", "IND" : "VIZAG", "UK" :"LONDON"}

print(type(name))
print(type(age))
print(type(salary))
print(type(fav_food))
print(type(fav_cars))
print(type(fav_places))