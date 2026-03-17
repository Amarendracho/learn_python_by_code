""" Python Functions are a block of statements that does a specific task. functions are used to
    repeated / common code tasks reuse. instead of same code write it again, and again we use functions to repeat.
"""

# We define a function using keyword called - def function_name:

def watching():
    print("WATCHING A WEB SERIES... GRAY'S ANATOMY")

# CALLING THE FUNCTION IS SIMPLE CALL WITH NAME OF THE FUNCTION.
watching()

# Function Arguments - Arguments are the values passed inside the parenthesis of the function.
#                      A function can have any number of arguments separated by a comma.

# Even / Odd check - SINGLE ARGUMENT
def evenCheck(n):
    if n % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

result = evenCheck(26)
print(result)

# TWO ARGUMENT
def multitasks(series, texting):
    print(f"I AM WATCHING {series} AND ALSO, I AM TEXTING IN {texting}")

multitasks("GRAY'S ANATOMY", "WHAT'S APP")


# Types of Function Arguments

# 1. DEFAULT ARGUMENTS - PASSING THE DEFAULT VALUE AS A FUNCTION PARAMETER.

def person(name, country = "USA"):
    print(name)
    print(country)

person("JUSTIN")

# 2. KEYWORD ARGUMENTS - PASSED BY EXPLICITLY SPECIFYING THE PARAMETER NAMES, SO THE ORDER DOESN’T MATTER

def customer(fname, lname):
    print(f"FIRST NAME: {fname}, LAST NAME: {lname}")

customer(fname="Alex", lname="Creav")
customer(fname="Justin", lname="Bieber")

def phoneDetails(brandName, modelName):


# 3. POSITIONAL ARGUMENTS - POSITIONAL ARGUMENTS, VALUES ARE ASSIGNED TO PARAMETERS BASED ON THEIR ORDER IN THE FUNCTION CALL.
#                           FALLOW THE ARGUMENT ORDER.
def employee(name, salary):
    print(f"Employee name is {name} & Salary is {salary}")

employee("Derek", 455000.21)
employee(234423.22, "Mark")

# 4. ARBITRARY ARGUMENTS - *args (KEYWORD ARGUMENTS)
#                          **kwargs (NON-KEYWORD ARGUMENTS)

# IF YOU ARE NOT SURE HOW MANY ARGUMENTS PASSING INSIDE () USE THESE 2.
"""*args and **kwargs are used when a function does not know in advance how many arguments it will receive"""

def unknow_parameters(*args):
    print(f"WE DON'T KNOW HOW MANY PARAMETER AS ARGUMENTS: {args}")
    for each in args:
        print(each)

unknow_parameters("A","B","C")

# KEY VALUE
def unknow_parameters2(**kwargs):
    print(f"WE DON'T KNOW HOW MANY PARAMETER AS ARGUMENTS: {kwargs}")
    for k,v in kwargs.items():
        print(k,v)

unknow_parameters2(key1 = "A", key2 = "B", key3 = "C")

def log(*messages):
    for msg in messages:
        print("LOG:", msg)

log("Server started")
log("User login", "UserID:123")

# FUNCTION WITHIN FUNCTIONS - A FUNCTION DEFINED INSIDE ANOTHER FUNCTION IS CALLED
#                               AN INNER FUNCTION (OR NESTED FUNCTION).

def outer():
    outer_var = "outer function"
    def inner():
        print(outer_var)
    inner()

outer()

# ANONYMOUS FUNCTIONS - FUNCTION WITHOUT NAME

# NORMAL FUNCTION
def add(a):
    print(a * a)

# LAMBDA FUNCTION
result = lambda a: print(a * a)

add(5)
result(6)

# RETURN STATEMENT IN FUNCTION - THE RETURN STATEMENT ENDS A FUNCTION AND SENDS A VALUE BACK TO THE CALLER.
#           IT CAN RETURN ANY DATA TYPE, MULTIPLE VALUES (PACKED INTO A TUPLE), OR NONE IF NO VALUE IS GIVEN

def square(num):
    return num ** num

print(square(3))


# RECURSIVE FUNCTIONS - A RECURSIVE FUNCTION IS A FUNCTION THAT CALLS ITSELF TO SOLVE A PROBLEM

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))