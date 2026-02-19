""" Few Common In-Build Exceptions
ValueError – wrong value format (e.g., int("abc"))
TypeError – wrong type usage (e.g., "1" + 2)
IndexError – list index out of range
KeyError – dict key missing
FileNotFoundError – file doesn’t exist
ZeroDivisionError – division by 0
AttributeError – missing attribute/method
ImportError / ModuleNotFoundError – import problems
All exceptions ultimately inherit from BaseException, but you usually catch from Exception.
"""

#BaseException - root exception rarely used in code.
try:
    raise BaseException("This is BaseException")
except BaseException as e:
    print(e)

#Exception  Class
# The Exception class is the base for all non-exit exceptions.
# You will often catch Exception in general error-handling code when you are not targeting a specific error type.
try:
    raise Exception("This is a generic exception")
except Exception as e:
    print(e)

# The ArithmeticError - class is the base for all errors related to mathematical operations.
try:
    raise ArithmeticError("This Error class throws math errors")
except ArithmeticError as e:
    print(e)

# ZeroDivisionError - A ZeroDivisionError occurs when you attempt to divide a number by zero.
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)

# OverflowError - An OverflowError occurs when the result of a numerical operation
#                 is too large for Python to represent. While Python handles large integers well,
#                 certain floating-point operations (like very large exponentials) can still cause this error.
import math
try:
    result = math.exp(1000)  # Exponential function with a large argument
except OverflowError as e:
    print(e)

# MemoryError - A MemoryError occurs when Python cannot allocate enough memory for an operation.
#               This usually happens when trying to create extremely large data structures.
# Don't run this code to system will hang
# try:
#     li = [1] * (10**10)
# except MemoryError as e:
#     print(e)