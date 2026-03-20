"""INNER FUNCTION - INNER FUNCTION IS A FUNCTION DEFINE INSIDE ANOTHER FUNCTION.
                    ALSO CALLED AS NESTED FUNCTION.
    USED FOR: ENCAPSULATION, ACCESS OUTER VARIABLES AND CLOSURES AND DECORATORS"""

# EXAMPLE INNER FUNCTION ACCESS VARIABLES FROM OUTER FUNCTION

def outer(name): # outer function
    def inner(): # inner function
        print(name) # access variable from outer scope
    inner()

outer("Amar")

# SCOPE OF VARIABLES IN INNER FUNCTIONS
# INNER FUNCTIONS FOLLOW PYTHON'S - LEGB RULE (LOCAL --> ENCLOSING --> GLOBAL --> BUILT-IN).
# INNER FUNCTIONS ACCESS OUTER FUNCTION VARIABLES, BUT MODIFYING THEM REQUIRES SPECIAL KEYWORDS LIKE (nonlocal).

# LOCAL VARIABLE ACCESS

def carBrand():
    brandName = "FORD MUSTANG"
    def carModel():
        print(brandName, "GT")
    carModel()

carBrand()

# MODIFYING VARIABLES USING NONLOCAL

def carBrand():
    brandName = "FORD MUSTANG"
    def carModel():
        nonlocal brandName #changeing outer variable value
        brandName = "PORSCHE"
        print(brandName)
    carModel()
    print(brandName, "911")

carBrand()

 # CLOSURE IN INNER FUNCTION

def carBrand(name):
    def carModel():
        print(name)
    return carModel # NOT CALLING INNER METHOD()

closure = carBrand("AUDI")
closure()

# EXAMPLE CLOSURE IN INNER FUNCTION

def outer_function(x):
    # Outer function: takes 'x' and defines inner_function
    def inner_function(y):
        return x + y  # 'x' is remembered from outer_function
    return inner_function  # Returns inner function (closure)

# Create a closure with x = 10
closure = outer_function(10)

# Call the closure with different values of 'y'
print(closure(5))
print(closure(20))

#ENCAPSULATION
def process_date(data):
    def clean_date():
        return [item.strip() for item in data]
    return clean_date()

print(process_date(["   HARRY ", "POTTER    ", "IS  BEST TV     ", "    SERIES"]))
