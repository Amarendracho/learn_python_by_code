# RECURSION - RECURSION IS A PROGRAMMING TECHNIQUE WHERE A FUNCTION CALLS ITSELF EITHER DIRECTLY OR INDIRECTLY
#             TO SOLVE A PROBLEM BY BREAKING IT INTO SMALLER, SIMPLER SUBPROBLEMS.

# WORKING OF RECURSION
#                  A RECURSIVE FUNCTION IS JUST LIKE ANY OTHER PYTHON FUNCTION EXCEPT THAT IT CALLS ITSELF IN ITS BODY.

                    # SYNTAX
"""def recursive_function(parameters):
    if base_case_condition:
        return base_result
    else:
        return recursive_function(modified_parameters)"""

"""RECURSIVE FUNCTION CONTAINS TWO KEY PARTS

    BASE CASE: THE STOPPING CONDITION THAT PREVENTS INFINITE RECURSION.
    RECURSIVE CASE: THE PART OF THE FUNCTION WHERE IT CALLS ITSELF WITH MODIFIED PARAMETERS."""

name = "Example 2: Fibonacci Sequence"
print(name.upper())

# EXAMPLE 1: FACTORIAL CALCULATION

def factorial(n):
    if n == 0: # BASE CONDITION
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# EXAMPLE 2: FIBONACCI SEQUENCE 5 = 5 + 4 + 3 + 2 + 1 = 15

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + fibonacci(n - 1)

print(fibonacci(10))