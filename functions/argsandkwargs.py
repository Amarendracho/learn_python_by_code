# *ARGS AND **KWARGS** - ARE USED WHEN A FUNCTION DOES NOT KNOW IN ADVANCE HOW MANY ARGUMENTS IT WILL RECEIVE.
#                       THEY ALLOW PYTHON FUNCTIONS TO ACCEPT VARIABLE NUMBER OF ARGUMENTS.


name = "They allow Python functions to accept variable number of arguments."
print(name.upper())

# NORMAL FUNCTION WITH FIXED ARGUMENTS
def add(a,b):
    return a+b

print(add(3,4))
# print(add(4,5,6)) # ERROR ADD() TAKES 2 ARGUMENTS