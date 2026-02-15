# exception is an event that interrupt the flow of the program.
#   when the exception happen the flow stop there and throw the exception.
#   [example: ZeroDivisionError, NameError, TypeError, ValueError]

# To Handle those errors we use [try , except, finally blocks]
        # use you think you block may throw an exception use [try:]
        # If you know what type of exception may occur use [except pre-defined exception: print("custom exception")].
        # [finally] block execute even the exception happen or not.


# 1 / 0 [ZeroDivisionError]
# 10 / name [NameError]
#20 + "coffee" [TypeError]
#int("something") [ValueError]

try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("I can execute any way")
