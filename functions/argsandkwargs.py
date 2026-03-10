# *ARGS AND **KWARGS** - ARE USED WHEN A FUNCTION DOES NOT KNOW IN ADVANCE HOW MANY ARGUMENTS IT WILL RECEIVE.
#                       THEY ALLOW PYTHON FUNCTIONS TO ACCEPT VARIABLE NUMBER OF ARGUMENTS.


name = "Python stores them in a tuple."
print(name.upper())

# NORMAL FUNCTION WITH FIXED ARGUMENTS
def add(a,b):
    return a+b

print(add(3,4))
# print(add(4,5,6)) # ERROR ADD() TAKES 2 ARGUMENTS


# *args - ALLOWS A FUNCTION TO ACCEPT MULTIPLE POSITIONAL ARGUMENTS.
#         PYTHON STORES THEM IN A TUPLE.

# SYNTAX - def function_name(*args)
def add(*args):
    return sum(args)

print(add(3,4,5,6,7,8,9))

