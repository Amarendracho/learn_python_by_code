                            # GLOBAL AND LOCAL VARIABLE

# LOCAL VARIABLE - LOCAL VARIABLES ARE CREATED INSIDE A FUNCTION AND EXIST ONLY DURING ITS EXECUTION.
#                  THEY CANNOT BE ACCESSED FROM OUTSIDE THE FUNCTION.

NAME = ("Global variables are declared outside all functions and can be accessed anywhere in the program,"
        " including inside functions.")

print(NAME.upper())

## LOCAL VARIABLE EXAMPLE

# def userDetails():
#     # LOCAL VARIABLES INIT AND DECLARATION
#     name = "Mark Slone"
#     age = 47
#     print(name, age)
#
# userDetails()

# # LOCAL VARIABLE CALLING OUTSIDE A METHOD
#
# def greeting():
#     message = "WELCOME TO LOCAL VARIABLES"
#     print(message)
#
# greeting()
# # print("OUTSIDE CALLING LOCAL VARIABLE :", message) - ERROR

# GLOBAL VARIABLE -