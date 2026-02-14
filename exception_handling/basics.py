"""Python Exception Handling allows a program to handle unexpected events (like invalid input or missing files)
        without crashing .
        Instead of terminating abruptly, Python lets you detect the problem, respond to it, and continue execution when possible.
"""
class Exception:

    try:
        a = 10
        b = 2
        print(a/b)

    except ZeroDivisionError:
        print("Don't do it")
