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

name = "Closure in inner function"
print(name.upper())

 # CLOSURE IN INNER FUNCTION

def carBrand():
    brandName = "FORD MUSTANG"
    def carModel():
        print(brandName, "GT")
    carModel()

carBrand()