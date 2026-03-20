"""INNER FUNCTION - INNER FUNCTION IS A FUNCTION DEFINE INSIDE ANOTHER FUNCTION.
                    ALSO CALLED AS NESTED FUNCTION.
    USED FOR: ENCAPSULATION, ACCESS OUTER VARIABLES AND CLOSURES AND DECORATORS"""

# EXAMPLE INNER FUNCTION ACCESS VARIABLES FROM OUTER FUNCTION

def outer(name): # outer function
    def inner(): # inner function
        print(name) # access variable from outer scope
    inner()

outer("Amar")