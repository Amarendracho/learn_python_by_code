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

name = "Recursive Case: The part of the function where it calls itself with modified parameters.."
print(name.upper())
