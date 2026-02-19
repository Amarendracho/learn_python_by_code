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