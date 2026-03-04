""" Python Functions are a block of statements that does a specific task. functions are used to
    repeated / common code tasks reuse. instead of same code write it again, and again we function to repeat.
"""

# We define a function using keyword called - def function_name:

# def watching():
#     print("WATCHING A WEB SERIES... GRAY'S ANATOMY")
#
# # CALLING THE FUNCTION IS SIMPLE CALL WITH NAME OF THE FUNCTION.
# watching()
#
# # Function Arguments - Arguments are the values passed inside the parenthesis of the function.
# #                      A function can have any number of arguments separated by a comma.
#
# # Even / Odd check - SINGLE ARGUMENT
# def evenCheck(n):
#     if n % 2 == 0:
#         return "EVEN"
#     else:
#         return "ODD"
#
# result = evenCheck(26)
# print(result)
#
# # TWO ARGUMENT
# def multitasks(series, texting):
#     print(f"I AM WATCHING {series} AND ALSO, I AM TEXTING IN {texting}")
#
# multitasks("GRAY'S ANATOMY", "WHAT'S APP")


# # Types of Function Arguments
#
# # 1. DEFAULT ARGUMENTS - PASSING THE DEFAULT VALUE INSIDE FUNCTION PARASITISM.
#
# def person(name, country = "USA"):
#     print(name, country)
#
# person("JUSTIN")

# # 2. KEYWORD ARGUMENTS - PASSED BY EXPLICITLY SPECIFYING THE PARAMETER NAMES, SO THE ORDER DOESN’T MATTER
#
# def customer(fname, lname):
#     print(f"FIRST NAME: {fname}, LAST NAME: {lname}")
#
# customer(fname="Alex", lname="Bob")
# customer(fname="Justin", lname="Bieber")

# # 3. POSITIONAL ARGUMENTS - POSITIONAL ARGUMENTS, VALUES ARE ASSIGNED TO PARAMETERS BASED ON THEIR ORDER IN THE FUNCTION CALL.
# #                           FALLOW THE ARGUMENT ORDER.
# def employee(name, salary):
#     print(f"Employee name is {name} & Salary is {salary}")
#
# employee("Derek", 455000.21)
# employee(234423.22, "Mark")

# 4. ARBITRARY ARGUMENTS - *args (KEYWORD ARGUMENTS)
#                          **kwargs (NON-KEYWORD ARGUMENTS)


name