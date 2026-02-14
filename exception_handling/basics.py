"""Python Exception Handling allows a program to handle unexpected events (like invalid input or missing files)
        without crashing .
        Instead of terminating abruptly, Python lets you detect the problem, respond to it, and continue execution when possible.
"""


# Exception example : ZeroDivisionError: division by zero
# a = 10
# b = 0
# print(a / b)

# To Handle those exceptions use try and except block. (try except)

class ExceptionExample:
    try:
        a = 10
        b = 2
        print(a/b)

    finally:
        pass

