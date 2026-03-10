# *ARGS AND **KWARGS** - ARE USED WHEN A FUNCTION DOES NOT KNOW IN ADVANCE HOW MANY ARGUMENTS IT WILL RECEIVE.
#                       THEY ALLOW PYTHON FUNCTIONS TO ACCEPT VARIABLE NUMBER OF ARGUMENTS.


name = "Python stores them in a dictionary."
print(name.upper())

# NORMAL FUNCTION WITH FIXED ARGUMENTS
def add(a,b):
    return a+b

print(add(3,4))
# print(add(4,5,6)) # ERROR ADD() TAKES 2 ARGUMENTS


# 1. *args - NON-KEYWORD ARGUMENTS, ALLOWS A FUNCTION TO ACCEPT MULTIPLE POSITIONAL ARGUMENTS.
#         PYTHON STORES THEM IN A TUPLE.

# # SYNTAX - def function_name(*args)
# def add_numbers(*args):
#     print(args)
#
# add_numbers(1,2,3,4)
#
# # ADD NUMBERS
# def add(*args):
#     return sum(args)
#
# print(add(3,4,5,6,7,8,9))
#
# # REAL USE
# def adding_numbers(*args):
#     total = 0
#     for number in args:
#         total += number
#     return total
#
# print(adding_numbers(10,20))
# print(adding_numbers(10,20,30))
# print(adding_numbers(10,20,30,40,50))

# def multiply(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result
#
# print(multiply(3,4))
# print(multiply(3,4,5))
# print(multiply(3,4,5,6))

# def names(*args):
#     for name in args:
#         print(name)
#
# names("PYTHON", "IS", "POWERFUL", "LANGUAGE FOR", "AI")

# 2. **kwargs - KEY WORD ARGUMENTS - ALLOWS A FUNCTION TO ACCEPT MULTIPLE KEYWORD ARGUMENTS.
#               PYTHON STORES THEM IN A DICTIONARY.

# SYNTAX - def function_name(**kwargs):

