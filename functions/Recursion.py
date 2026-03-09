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

Base Case: The stopping condition that prevents infinite recursion.
Recursive Case: The part of the function where it calls itself with modified parameters."""

name = "Base Case: The stopping condition that prevents infinite recursion."
print(name.upper())
