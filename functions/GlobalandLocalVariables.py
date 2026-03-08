                            # GLOBAL AND LOCAL VARIABLE

# LOCAL VARIABLE - LOCAL VARIABLES ARE CREATED INSIDE A FUNCTION AND EXIST ONLY DURING ITS EXECUTION.
#                  THEY CANNOT BE ACCESSED FROM OUTSIDE THE FUNCTION.

NAME = "Modifying Global Variables Inside a Function"

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

# GLOBAL VARIABLE - GLOBAL VARIABLES ARE DECLARED OUTSIDE ALL FUNCTIONS AND CAN BE ACCESSED ANYWHERE IN THE PROGRAM,
#                   INCLUDING INSIDE FUNCTIONS.

# msg = "THIS IS GLOBAL VARIABLE ACCESS INSIDE A FUNCTION AND OUTSIDE A FUNCTION"
#
# def greet():
#     print("INSIDE A FUNCTION - ",msg)
#
# greet()
# print("OUTSIDE A FUNCTION - ",msg)

# MODIFYING GLOBAL VARIABLES INSIDE A FUNCTION - BY DEFAULT WE CANNOT MODIFY GLOBAL VARIABLES INSIDE A FUNCTION.
#                                                WITH THE HELP OF global DECLARATION WE CAN CHANGE IT.

# WITHOUT global DECLARATION

# country = "UNITED STATES"
# def userInfo():
#     # ERROR - UnboundLocalError
#     # country += "MARK"
#     #  print(country)
#     pass

# WITH global DECLARATION

