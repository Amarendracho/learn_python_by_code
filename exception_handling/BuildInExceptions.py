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

