"""Python Exception Handling allows a program to handle unexpected events (like invalid input or missing files)
        without crashing .
        Instead of terminating abruptly, Python lets you detect the problem, respond to it, and continue execution when possible.
"""
from contextlib import nullcontext


# Exception example : ZeroDivisionError: division by zero
# a = 10
# b = 0
# print(a / b)

# To Handle those exceptions use try and except block. (try except)

class ExceptionExample:
    try:
        a = 10
        b = 0
        print(a/b)

    except ZeroDivisionError:
        print("Number can't divide by zero 🛑")

# Dividing a number by 0 raises a ZeroDivisionError.
# The try block contains code that may fail
# The except block catches the error, printing a safe message instead of stopping the program.

# ERROR VS EXCEPTION

#ERRORS :  Serious problems in the program logic that cannot be handled. Examples include syntax errors or memory errors.
# name =                # syntax error - expression expected
# print(name            # syntax error - ')' expected

# EXCEPTION - problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).
n = 10
#res = n / 0         # ZeroDivisionError (Exception)

name = ""
print(name.)
